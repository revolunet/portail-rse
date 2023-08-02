from datetime import date

import pytest

from entreprises.models import ActualisationCaracteristiquesAnnuelles
from entreprises.models import CaracteristiquesAnnuelles
from entreprises.models import Entreprise


@pytest.fixture
def alice(django_user_model):
    alice = django_user_model.objects.create(
        prenom="Alice",
        nom="Cooper",
        email="alice@impact.test",
        reception_actualites=False,
        is_email_confirmed=True,
    )
    return alice


@pytest.fixture
def bob(django_user_model):
    bob = django_user_model.objects.create(
        prenom="Bob",
        nom="Dylan",
        email="bob@impact.test",
        reception_actualites=False,
        is_email_confirmed=True,
    )
    return bob


@pytest.fixture
def entreprise_non_qualifiee(alice):
    entreprise = Entreprise.objects.create(
        siren="000000001", denomination="Entreprise SAS"
    )
    return entreprise


@pytest.fixture
def date_cloture_dernier_exercice():
    return date(2022, 12, 31)


@pytest.fixture
def entreprise_factory(db, date_cloture_dernier_exercice):
    def create_entreprise(
        siren="000000001",
        denomination="Entreprise SAS",
        date_cloture_exercice=date_cloture_dernier_exercice,
        appartient_groupe=False,
        comptes_consolides=False,
        effectif=CaracteristiquesAnnuelles.EFFECTIF_MOINS_DE_50,
        effectif_outre_mer=CaracteristiquesAnnuelles.EFFECTIF_OUTRE_MER_MOINS_DE_250,
        tranche_chiffre_affaires=CaracteristiquesAnnuelles.CA_MOINS_DE_700K,
        tranche_bilan=CaracteristiquesAnnuelles.BILAN_MOINS_DE_350K,
        tranche_chiffre_affaires_consolide=CaracteristiquesAnnuelles.CA_MOINS_DE_700K,
        tranche_bilan_consolide=CaracteristiquesAnnuelles.BILAN_MOINS_DE_350K,
        bdese_accord=False,
        systeme_management_energie=False,
    ):
        entreprise = Entreprise.objects.create(
            siren=siren,
            denomination=denomination,
            date_cloture_exercice=date_cloture_exercice,
            appartient_groupe=appartient_groupe,
            comptes_consolides=comptes_consolides,
        )
        actualisation = ActualisationCaracteristiquesAnnuelles(
            date_cloture_exercice,
            effectif,
            effectif_outre_mer,
            tranche_chiffre_affaires,
            tranche_bilan,
            tranche_chiffre_affaires_consolide if comptes_consolides else None,
            tranche_bilan_consolide if comptes_consolides else None,
            bdese_accord,
            systeme_management_energie,
        )
        caracteristiques = entreprise.actualise_caracteristiques(actualisation)
        caracteristiques.save()
        return entreprise

    return create_entreprise
