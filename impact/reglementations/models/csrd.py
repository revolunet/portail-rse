from django.conf import settings
from django.db import models

from entreprises.models import Entreprise
from utils.models import TimestampedModel


class CSRD(TimestampedModel):
    annee = models.IntegerField()
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    themes_durabilite = models.JSONField(
        null=True,
        blank=True,
    )
