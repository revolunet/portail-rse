from datetime import date

import requests
import sentry_sdk

from api.exceptions import APIError
from entreprises.models import CaracteristiquesAnnuelles

RATIOS_FINANCIERS_TIMEOUT = 10


def dernier_exercice_comptable(siren):
    donnees_financieres = {
        "date_cloture_exercice": None,
        "tranche_chiffre_affaires": None,
        "tranche_chiffre_affaires_consolide": None,
    }
    try:
        response = requests.get(
            "https://data.economie.gouv.fr/api/records/1.0/search/",
            params={
                "dataset": "ratios_inpi_bce",
                "q": f"siren={siren}",
                "sort": "date_cloture_exercice",
            },
            timeout=RATIOS_FINANCIERS_TIMEOUT,
        )
    except Exception as e:
        with sentry_sdk.push_scope() as scope:
            scope.set_level("info")
            sentry_sdk.capture_exception(e)
        raise APIError()

    try:
        record = response.json()["records"][0]
        fields = record["fields"]
        donnees_financieres["date_cloture_exercice"] = _extrait_date_cloture_extercice(
            fields
        )
        df = _extrait_chiffres_affaires(fields)
        donnees_financieres.update(df)
    except IndexError:
        pass

    try:
        record = response.json()["records"][1]
        fields = record["fields"]
        date_cloture_exercice = _extrait_date_cloture_extercice(fields)
        if date_cloture_exercice == donnees_financieres["date_cloture_exercice"]:
            df = _extrait_chiffres_affaires(fields)
            donnees_financieres.update(df)
    except IndexError:
        pass
    return donnees_financieres


def _extrait_date_cloture_extercice(fields):
    return date.fromisoformat(fields["date_cloture_exercice"])


def _extrait_chiffres_affaires(fields):
    donnees_financieres = {}
    chiffre_affaires = int(fields["chiffre_d_affaires"])
    type_bilan = fields["type_bilan"]
    if type_bilan in ("C", "S"):  # bilan complet ou simplifié
        if chiffre_affaires < 900_000:  # 0-900k
            tranche_chiffre_affaires = CaracteristiquesAnnuelles.CA_MOINS_DE_900K
        elif chiffre_affaires < 50_000_000:  # 900k-50M
            tranche_chiffre_affaires = CaracteristiquesAnnuelles.CA_ENTRE_900K_ET_50M
        elif chiffre_affaires < 100_000_000:  # 50M-100M
            tranche_chiffre_affaires = CaracteristiquesAnnuelles.CA_ENTRE_50M_ET_100M
        else:  # 100M+
            tranche_chiffre_affaires = CaracteristiquesAnnuelles.CA_100M_ET_PLUS
        donnees_financieres["tranche_chiffre_affaires"] = tranche_chiffre_affaires
    elif type_bilan == "K":  # bilan consolidé
        if chiffre_affaires < 60_000_000:  # 0-60M
            tranche_chiffre_affaires_consolide = (
                CaracteristiquesAnnuelles.CA_MOINS_DE_60M
            )
        elif chiffre_affaires < 100_000_000:  # 60M-100M
            tranche_chiffre_affaires_consolide = (
                CaracteristiquesAnnuelles.CA_ENTRE_60M_ET_100M
            )
        else:  # 100M+
            tranche_chiffre_affaires_consolide = (
                CaracteristiquesAnnuelles.CA_100M_ET_PLUS
            )
        donnees_financieres[
            "tranche_chiffre_affaires_consolide"
        ] = tranche_chiffre_affaires_consolide
    return donnees_financieres
