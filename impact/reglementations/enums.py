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
        description="L’adaptation au changement climatique renvoie au processus d’adaptation de l’entreprise au changement climatique réel et attendu",
    ),
    EnjeuNormalise(
        esrs=ESRS.ESRS_E1,
        nom="Atténuation du changement climatique",
        description="L’atténuation du changement climatique se réfère aux efforts de l’entreprise en faveur du processus général consistant à limiter l’élévation de la température moyenne de la planète à 1,5° C par rapport aux niveaux préindustriels, conformément à l’accord de Paris. La présente norme couvre les exigences de publication liées, notamment, aux sept gaz à effet de serre (GES) que sont le dioxyde de carbone (CO2), le méthane (CH4), le protoxyde d’azote (N2O), les hydrofluorocarbures (HFC), les hydrocarbures perfluorés (PFC), l’hexafluorure de soufre (SF6) et le trifluorure d’azote (NF3). Elle couvre également les exigences de publication portant sur la manière dont l’entreprise gère ses émissions de GES ainsi que les risques de transition qui y sont associés",
    ),
    EnjeuNormalise(
        esrs=ESRS.ESRS_E1,
        nom="Énergie",
        description="Les exigences de publication relatives à l’« énergie » couvrent toutes les formes de production et de consommation d’énergie.",
    ),
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
    EnjeuNormalise(esrs=ESRS.ESRS_E4, nom="Incidence sur l'état des espèces"),
    EnjeuNormalise(
        esrs=ESRS.ESRS_E4, nom="Incidence sur l'étendue et l'état des écosystèmes"
    ),
]
