from datetime import date

import api.exceptions
from api.tests.fixtures import mock_api_infos_entreprise  # noqa
from conftest import CODE_PAYS_PORTUGAL
from entreprises.models import CaracteristiquesAnnuelles


def test_succes_api_search_entreprise(client, mock_api_infos_entreprise):
    siren = "123456789"
    mock_api_infos_entreprise.return_value = {
        "siren": siren,
        "denomination": "Entreprise SAS",
        "effectif": CaracteristiquesAnnuelles.EFFECTIF_MOINS_DE_10,
        "categorie_juridique_sirene": 5710,
        "code_pays_etranger_sirene": CODE_PAYS_PORTUGAL,
        "code_NAF": "01.11Z",
        "date_cloture_exercice": date(2023, 12, 31),
        "tranche_chiffre_affaires": CaracteristiquesAnnuelles.CA_MOINS_DE_900K,
        "tranche_chiffre_affaires_consolide": CaracteristiquesAnnuelles.CA_MOINS_DE_60M,
    }

    response = client.get(f"/api/search-entreprise/{siren}")

    mock_api_infos_entreprise.assert_called_once_with(siren, donnees_financieres=True)
    assert response.status_code == 200
    assert response.json() == {
        "siren": siren,
        "denomination": "Entreprise SAS",
        "effectif": CaracteristiquesAnnuelles.EFFECTIF_MOINS_DE_10,
        "categorie_juridique_sirene": 5710,
        "code_pays_etranger_sirene": CODE_PAYS_PORTUGAL,
        "code_NAF": "01.11Z",
        "date_cloture_exercice": "2023-12-31",
        "tranche_chiffre_affaires": CaracteristiquesAnnuelles.CA_MOINS_DE_900K,
        "tranche_chiffre_affaires_consolide": CaracteristiquesAnnuelles.CA_MOINS_DE_60M,
    }


def test_echec_api_search_entreprise_car_l_API_infos_entreprise_est_en_erreur(
    client, mock_api_infos_entreprise
):
    mock_api_infos_entreprise.side_effect = api.exceptions.APIError("Panne serveur")

    response = client.get("/api/search-entreprise/123456789")

    assert response.status_code == 400
    assert response.json() == {
        "error": "Panne serveur",
    }
