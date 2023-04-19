from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from utils.models import TimestampedModel

DENOMINATION_MAX_LENGTH = 250
FONCTIONS_MAX_LENGTH = 250


class Entreprise(TimestampedModel):
    EFFECTIF_MOINS_DE_50 = "0-49"
    EFFECTIF_ENTRE_50_ET_299 = "50-299"
    EFFECTIF_ENTRE_300_ET_499 = "300-499"
    EFFECTIF_PLUS_DE_500 = "500+"
    EFFECTIF_CHOICES = [
        (EFFECTIF_MOINS_DE_50, "moins de 50"),
        (EFFECTIF_ENTRE_50_ET_299, "entre 50 et 299"),
        (EFFECTIF_ENTRE_300_ET_499, "entre 300 et 499"),
        (EFFECTIF_PLUS_DE_500, "plus de 500"),
    ]

    siren = models.CharField(max_length=9, unique=True)
    denomination = models.CharField(max_length=DENOMINATION_MAX_LENGTH)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="habilitations.Habilitation"
    )
    effectif = models.CharField(
        max_length=9,
        choices=EFFECTIF_CHOICES,
        help_text="Vérifiez et confirmez le nombre de salariés",
        null=True,
    )
    bdese_accord = models.BooleanField(
        verbose_name="L'entreprise a un accord collectif d'entreprise concernant la Base de Données Économiques, Sociales et Environnementales (BDESE)",
        default=False,
    )

    def __str__(self):
        return f"{self.siren} {self.denomination}"

    @property
    def is_qualified(self):
        return self.denomination and self.effectif
