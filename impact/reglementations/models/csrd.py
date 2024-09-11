import django.db.models as models
from django.core.validators import MinValueValidator

from ..enums import EnjeuNormalise
from ..enums import ENJEUX_NORMALISES
from ..enums import ESRS
from utils.models import TimestampedModel


class RapportCSRD(TimestampedModel):
    habilitation = models.ForeignKey(
        "habilitations.Habilitation", on_delete=models.CASCADE, related_name="rapports"
    )
    entreprise = models.ForeignKey("entreprises.Entreprise", on_delete=models.CASCADE)

    annee = models.PositiveIntegerField(
        verbose_name="année du rapport CSRD", validators=[MinValueValidator(2024)]
    )
    description = models.TextField(
        verbose_name="description du rapport CSRD", blank=True
    )

    class Meta:
        verbose_name = "rapport CSRD"
        unique_together = [["annee", "habilitation"]]
        indexes = [models.Index(fields=["annee"])]

    def __str__(self):
        return f"CRSD {self.annee} - {self.habilitation}"

    def _init_enjeux(self):
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

    def save(self, *args, **kwargs):
        enjeux = self._init_enjeux()

        super().save(*args, **kwargs)

        if enjeux:
            self.enjeux.add(*enjeux, bulk=False)


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


def rapport_csrd_personnel(habilitation):  # ajouter l'année ?
    return RapportCSRD.objects.filter(habilitation=habilitation).first()
