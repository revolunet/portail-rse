import django.db.models as models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from ..enums import EnjeuNormalise
from ..enums import ENJEUX_NORMALISES
from ..enums import ESRS
from utils.models import TimestampedModel


class RapportCSRDQuerySet(models.QuerySet):
    def annee(self, annee: int):
        return self.filter(annee=annee)

    def principaux(self):
        return self.filter(proprietaire=None)

    def personnels(self):
        return self.exclude(proprietaire=None)

    ...


class RapportCSRD(TimestampedModel):
    entreprise = models.ForeignKey(
        "entreprises.Entreprise",
        on_delete=models.CASCADE,
        related_name="rapports_csrd",
    )
    proprietaire = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="propriétaire rapport CSRD personnel",
    )
    annee = models.PositiveIntegerField(
        verbose_name="année du rapport CSRD", validators=[MinValueValidator(2024)]
    )
    description = models.TextField(
        verbose_name="description du rapport CSRD", blank=True
    )

    objects = RapportCSRDQuerySet.as_manager()

    class Meta:
        verbose_name = "rapport CSRD"
        unique_together = [["annee", "entreprise", "proprietaire"]]
        indexes = [models.Index(fields=["annee"])]

    def __str__(self):
        return f"CRSD {self.annee} - {self.entreprise}"

    def _init_enjeux(self):
        # ajoute les enjeux "réglementés" lors de la création de l'instance
        if self.pk:
            # uniquement pour la création initiale de l'objet
            return

        # on ajoute les enjeux normalisés des ESRD
        tmp_enjeux = []

        def _add_enjeux(enjeux: list[EnjeuNormalise], parent=None):
            for idx, enjeu in enumerate(enjeux, 1):
                ne = Enjeu(
                    esrs=enjeu.esrs,
                    nom=enjeu.nom,
                    description=enjeu.description,
                    parent=parent,
                    modifiable=False,
                    ordre=idx,
                )
                tmp_enjeux.append(ne)

            if not enjeu.children:
                return

            _add_enjeux(enjeu.children, ne)

        _add_enjeux(ENJEUX_NORMALISES)

        return tmp_enjeux

    def clean(self):
        # La vérification du rapport principal pourrait être faite par une contrainte (complexe)
        # en base de données, mais le fait d'utiliser une validation métier vérifiable
        # à tout moment est plus simple et plus lisible.
        already_exists = RapportCSRD.objects.filter(
            proprietaire=None, entreprise=self.entreprise
        ).exists()

        if not self.proprietaire and already_exists:
            raise ValidationError(
                "Il existe déjà un rapport CSRD principal pour cette entreprise"
            )

        if self.pk and already_exists and self.proprietaire:
            raise ValidationError(
                "Impossible de modifier le rapport CSRD principal en rapport personnel"
            )

        ...

    def save(self, *args, **kwargs):
        enjeux = self._init_enjeux()

        # on vérifie systématiquement les contraintes métiers avant la sauvegarde
        self.clean()
        super().save(*args, **kwargs)

        if enjeux:
            self.enjeux.add(*enjeux, bulk=False)

    def is_principal(self):
        # le rapport CSRD n'a un propriétaire que si c'est un rapport personnel
        return self.pk and not self.proprietaire


class EnjeuQuerySet(models.QuerySet):
    def selectionnes(self):
        return self.filter(selection=True).order_by("ordre")

    def modifiables(self):
        return self.filter(modifiable=True).order_by("ordre")

    ...


class Enjeu(TimestampedModel):
    rapport_csrd = models.ForeignKey(
        "RapportCSRD", on_delete=models.CASCADE, related_name="enjeux"
    )
    parent = models.ForeignKey(
        "Enjeu", null=True, on_delete=models.CASCADE, verbose_name="enjeu parent"
    )
    esrs = models.TextField(choices=ESRS.choices, verbose_name="ESRS rattaché")

    nom = models.TextField(verbose_name="nom de l'enjeu")
    description = models.TextField(verbose_name="description de l'enjeu", blank=True)
    modifiable = models.BooleanField(
        verbose_name="enjeu modifiable par l'utilisateur", default=True
    )
    selection = models.BooleanField(verbose_name="selectionné", default=False)
    ordre = models.PositiveIntegerField(verbose_name="ordre d'affichage")

    class Meta:
        verbose_name = "enjeu ESRS"
        unique_together = [["rapport_csrd", "nom"]]
        indexes = [models.Index(fields=["esrs"])]
        ordering = ["rapport_csrd", "ordre"]

    objects = EnjeuQuerySet.as_manager()

    def __str__(self):
        return f"{self.esrs} - {self.nom}"


def rapport_csrd_officiel(entreprise):  # ajouter l'année ?
    return RapportCSRD.objects.filter(entreprise=entreprise).first()


def rapport_csrd_personnel(entreprise, proprietaire):  # ajouter l'année ?
    return RapportCSRD.objects.filter(
        entreprise=entreprise, proprietaire=proprietaire
    ).first()
