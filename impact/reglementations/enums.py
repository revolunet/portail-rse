from dataclasses import dataclass
from dataclasses import field

import django.db.models as models


class ESRS(models.TextChoices):
    ESRS_1 = "ESRS_1"
    ESRS_2 = "ESRS_2"

    ESRS_E1 = "ESRS_E1"
    ESRS_E2 = "ESRS_E2"
    ESRS_E3 = "ESRS_E3"
    ESRS_E4 = "ESRS_E4"
    ESRS_E5 = "ESRS_E5"

    ESRS_S1 = "ESRS_S1"
    ESRS_S2 = "ESRS_S2"
    ESRS_S3 = "ESRS_S3"
    ESRS_S4 = "ESRS_S4"

    ESRS_G1 = "ESRS_G1"


@dataclass
class EnjeuNormalise:
    esrs: ESRS
    nom: str
    children: list["EnjeuNormalise"] = field(default_factory=list)
    description: str = ""


# proposition :
# enjeux ajoutés automatiquement à la création d'un nouveau rapport CSRD

ENJEUX_NORMALISES = [
    # Structure simple :
    EnjeuNormalise(
        esrs=ESRS.ESRS_E1,
        nom="Adaptation au changement climatique",
        description="whatever",
    ),
    EnjeuNormalise(esrs=ESRS.ESRS_E1, nom="Atténuation du changement climatique"),
    EnjeuNormalise(esrs=ESRS.ESRS_E1, nom="Énergie"),
    # Structure hiérarchisée :
    EnjeuNormalise(
        esrs=ESRS.ESRS_E4,
        nom="Vecteurs directs de perte de biodiversité",
        children=[
            EnjeuNormalise(esrs=ESRS.ESRS_E4, nom="Changement climatique"),
            EnjeuNormalise(
                esrs=ESRS.ESRS_E4,
                nom="Changement d’affectation des terres, changement d’utilisation de l’eau douce et des mers",
            ),
            EnjeuNormalise(esrs=ESRS.ESRS_E4, nom="Exploitation directe"),
            EnjeuNormalise(esrs=ESRS.ESRS_E4, nom="Espèces exotiques envahissantes"),
            EnjeuNormalise(esrs=ESRS.ESRS_E4, nom="Pollution"),
            EnjeuNormalise(esrs=ESRS.ESRS_E4, nom="Autres"),
        ],
    ),
]

"""

"""
