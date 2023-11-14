import pytest
from django.urls import reverse

from entreprises.models import CaracteristiquesAnnuelles
from reglementations.views.dpef import DPEFReglementation


def test_dpef_reglementation_info():
    info = DPEFReglementation.info()

    assert info["title"] == "Déclaration de Performance Extra-Financière"

    assert (
        info["description"]
        == """La Déclaration de Performance Extra-Financière (dite "DPEF") est un document par l'intermédiaire duquel une entreprise détaille les implications sociales, environnementales et sociétales de sa performance et de ses activités, ainsi que son mode de gouvernance."""
    )
    assert info["more_info_url"] == reverse("reglementations:fiche_dpef")


@pytest.mark.parametrize(
    "effectif_permanent",
    [
        CaracteristiquesAnnuelles.EFFECTIF_ENTRE_500_ET_4999,
        CaracteristiquesAnnuelles.EFFECTIF_ENTRE_5000_ET_9999,
        CaracteristiquesAnnuelles.EFFECTIF_10000_ET_PLUS,
    ],
)
def test_soumis_avec_effectif_permanent_et_bilan_suffisants(
    effectif_permanent, entreprise_factory
):
    entreprise = entreprise_factory(
        effectif_permanent=effectif_permanent,
        tranche_bilan=CaracteristiquesAnnuelles.BILAN_100M_ET_PLUS,
        tranche_chiffre_affaires=CaracteristiquesAnnuelles.CA_MOINS_DE_700K,
    )

    soumis = DPEFReglementation.est_soumis(
        entreprise.dernieres_caracteristiques_qualifiantes
    )

    assert soumis


@pytest.mark.parametrize(
    "effectif_permanent",
    [
        CaracteristiquesAnnuelles.EFFECTIF_ENTRE_500_ET_4999,
        CaracteristiquesAnnuelles.EFFECTIF_ENTRE_5000_ET_9999,
        CaracteristiquesAnnuelles.EFFECTIF_10000_ET_PLUS,
    ],
)
def test_soumis_avec_effectif_permanent_et_ca_suffisants(
    effectif_permanent, entreprise_factory
):
    entreprise = entreprise_factory(
        effectif_permanent=effectif_permanent,
        tranche_bilan=CaracteristiquesAnnuelles.BILAN_MOINS_DE_350K,
        tranche_chiffre_affaires=CaracteristiquesAnnuelles.CA_100M_ET_PLUS,
    )

    soumis = DPEFReglementation.est_soumis(
        entreprise.dernieres_caracteristiques_qualifiantes
    )

    assert soumis


@pytest.mark.parametrize(
    "effectif_permanent",
    [
        CaracteristiquesAnnuelles.EFFECTIF_ENTRE_500_ET_4999,
        CaracteristiquesAnnuelles.EFFECTIF_ENTRE_5000_ET_9999,
        CaracteristiquesAnnuelles.EFFECTIF_10000_ET_PLUS,
    ],
)
def test_soumis_avec_effectif_permanent_bilan_et_ca_suffisants(
    effectif_permanent, entreprise_factory
):
    entreprise = entreprise_factory(
        effectif_permanent=effectif_permanent,
        tranche_bilan=CaracteristiquesAnnuelles.BILAN_100M_ET_PLUS,
        tranche_chiffre_affaires=CaracteristiquesAnnuelles.CA_100M_ET_PLUS,
    )

    soumis = DPEFReglementation.est_soumis(
        entreprise.dernieres_caracteristiques_qualifiantes
    )

    assert soumis


@pytest.mark.parametrize(
    "effectif_permanent",
    [
        CaracteristiquesAnnuelles.EFFECTIF_MOINS_DE_50,
        CaracteristiquesAnnuelles.EFFECTIF_ENTRE_50_ET_249,
        CaracteristiquesAnnuelles.EFFECTIF_ENTRE_250_ET_299,
        CaracteristiquesAnnuelles.EFFECTIF_ENTRE_300_ET_499,
    ],
)
def test_non_soumis_car_effectif_permanent_insuffisant(
    effectif_permanent, entreprise_factory
):
    entreprise = entreprise_factory(
        effectif_permanent=effectif_permanent,
        tranche_bilan=CaracteristiquesAnnuelles.BILAN_100M_ET_PLUS,
        tranche_chiffre_affaires=CaracteristiquesAnnuelles.CA_100M_ET_PLUS,
    )

    soumis = DPEFReglementation.est_soumis(
        entreprise.dernieres_caracteristiques_qualifiantes
    )

    assert not soumis
