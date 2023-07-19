from datetime import date
from datetime import datetime
from datetime import timedelta
from datetime import timezone

import pytest
from django.db import IntegrityError
from freezegun import freeze_time

from entreprises.models import ActualisationCaracteristiquesAnnuelles
from entreprises.models import CaracteristiquesAnnuelles
from entreprises.models import categorie
from entreprises.models import CategorieJuridique
from entreprises.models import Entreprise


@pytest.mark.django_db(transaction=True)
def test_entreprise():
    now = datetime(2023, 1, 27, 16, 1, tzinfo=timezone.utc)

    with freeze_time(now):
        entreprise = Entreprise.objects.create(
            siren="123456789",
            denomination="Entreprise SAS",
            date_cloture_exercice=date(2023, 7, 7),
            appartient_groupe=False,
            comptes_consolides=False,
        )

    assert entreprise.created_at == now
    assert entreprise.updated_at == now
    assert entreprise.siren == "123456789"
    assert entreprise.denomination == "Entreprise SAS"
    assert entreprise.date_cloture_exercice == date(2023, 7, 7)
    assert entreprise.appartient_groupe is False
    assert entreprise.comptes_consolides is False
    assert not entreprise.users.all()

    with pytest.raises(IntegrityError):
        Entreprise.objects.create(
            siren="123456789", denomination="Autre Entreprise SAS"
        )

    with freeze_time(now + timedelta(1)):
        entreprise.denomination = "Nouveau nom SAS"
        entreprise.save()

    assert entreprise.updated_at == now + timedelta(1)


def test_caracteristiques_ne_sont_pas_qualifiantes_tant_que_groupe_non_qualifie(
    entreprise_non_qualifiee,
):
    entreprise_non_qualifiee.appartient_groupe = None
    entreprise_non_qualifiee.societe_mere_en_france = None
    entreprise_non_qualifiee.comptes_consolides = None

    caracteristiques = CaracteristiquesAnnuelles(
        entreprise=entreprise_non_qualifiee,
        date_cloture_exercice=date(2023, 7, 7),
        effectif=CaracteristiquesAnnuelles.EFFECTIF_MOINS_DE_50,
        effectif_outre_mer=CaracteristiquesAnnuelles.EFFECTIF_OUTRE_MER_MOINS_DE_250,
        effectif_groupe=CaracteristiquesAnnuelles.EFFECTIF_ENTRE_250_ET_499,
        tranche_chiffre_affaires=CaracteristiquesAnnuelles.CA_MOINS_DE_700K,
        tranche_bilan=CaracteristiquesAnnuelles.BILAN_MOINS_DE_350K,
        bdese_accord=True,
        systeme_management_energie=True,
    )

    assert not caracteristiques.groupe_est_qualifie
    assert not caracteristiques.sont_qualifiantes

    entreprise_non_qualifiee.appartient_groupe = True

    assert not caracteristiques.groupe_est_qualifie
    assert not caracteristiques.sont_qualifiantes

    entreprise_non_qualifiee.comptes_consolides = False

    assert not caracteristiques.groupe_est_qualifie
    assert not caracteristiques.sont_qualifiantes

    entreprise_non_qualifiee.societe_mere_en_france = False

    assert caracteristiques.groupe_est_qualifie
    assert caracteristiques.sont_qualifiantes


def test_caracteristiques_sont_qualifiantes_si_entreprise_n_appartient_pas_groupe(
    entreprise_non_qualifiee,
):
    entreprise_non_qualifiee.appartient_groupe = False

    caracteristiques = CaracteristiquesAnnuelles(
        entreprise=entreprise_non_qualifiee,
        date_cloture_exercice=date(2023, 7, 7),
        effectif=CaracteristiquesAnnuelles.EFFECTIF_MOINS_DE_50,
        effectif_outre_mer=CaracteristiquesAnnuelles.EFFECTIF_OUTRE_MER_MOINS_DE_250,
        tranche_chiffre_affaires=CaracteristiquesAnnuelles.CA_MOINS_DE_700K,
        tranche_bilan=CaracteristiquesAnnuelles.BILAN_MOINS_DE_350K,
        bdese_accord=True,
        systeme_management_energie=True,
    )

    assert caracteristiques.sont_qualifiantes


def test_caracteristiques_sont_qualifiantes_si_entreprise_appartient_groupe(
    entreprise_non_qualifiee,
):
    entreprise_non_qualifiee.appartient_groupe = True
    entreprise_non_qualifiee.societe_mere_en_france = False
    entreprise_non_qualifiee.comptes_consolides = False

    caracteristiques = CaracteristiquesAnnuelles(
        entreprise=entreprise_non_qualifiee,
        date_cloture_exercice=date(2023, 7, 7),
        effectif=CaracteristiquesAnnuelles.EFFECTIF_MOINS_DE_50,
        effectif_outre_mer=CaracteristiquesAnnuelles.EFFECTIF_OUTRE_MER_MOINS_DE_250,
        tranche_chiffre_affaires=CaracteristiquesAnnuelles.CA_MOINS_DE_700K,
        tranche_bilan=CaracteristiquesAnnuelles.BILAN_MOINS_DE_350K,
        bdese_accord=True,
        systeme_management_energie=True,
    )

    assert not caracteristiques.sont_qualifiantes

    caracteristiques.effectif_groupe = (
        CaracteristiquesAnnuelles.EFFECTIF_ENTRE_250_ET_499
    )

    assert caracteristiques.sont_qualifiantes

    entreprise_non_qualifiee.comptes_consolides = True

    assert not caracteristiques.sont_qualifiantes

    caracteristiques.tranche_chiffre_affaires_consolide = (
        CaracteristiquesAnnuelles.CA_MOINS_DE_700K
    )
    caracteristiques.tranche_bilan_consolide = (
        CaracteristiquesAnnuelles.BILAN_MOINS_DE_350K
    )

    assert caracteristiques.sont_qualifiantes


@pytest.mark.django_db(transaction=True)
def test_dernieres_caracteristiques_qualifiantes(entreprise_non_qualifiee):
    assert entreprise_non_qualifiee.dernieres_caracteristiques_qualifiantes is None

    entreprise_non_qualifiee.appartient_groupe = False
    entreprise_non_qualifiee.comptes_consolides = False
    entreprise_non_qualifiee.save()
    actualisation = ActualisationCaracteristiquesAnnuelles(
        date_cloture_exercice=date(2023, 7, 7),
        effectif=CaracteristiquesAnnuelles.EFFECTIF_MOINS_DE_50,
        effectif_outre_mer=CaracteristiquesAnnuelles.EFFECTIF_OUTRE_MER_MOINS_DE_250,
        effectif_groupe=None,
        tranche_chiffre_affaires=CaracteristiquesAnnuelles.CA_MOINS_DE_700K,
        tranche_bilan=CaracteristiquesAnnuelles.BILAN_MOINS_DE_350K,
        tranche_chiffre_affaires_consolide=None,
        tranche_bilan_consolide=None,
        bdese_accord=True,
        systeme_management_energie=True,
    )
    caracteristiques_2023 = entreprise_non_qualifiee.actualise_caracteristiques(
        actualisation
    )
    caracteristiques_2023.save()

    with freeze_time(date(2025, 1, 27)):
        assert (
            entreprise_non_qualifiee.dernieres_caracteristiques_qualifiantes
            == caracteristiques_2023
        )

    caracteristiques_2024 = CaracteristiquesAnnuelles(
        annee=2024,
        entreprise=entreprise_non_qualifiee,
    )
    caracteristiques_2024.save()

    with freeze_time(date(2025, 1, 27)):
        assert (
            entreprise_non_qualifiee.dernieres_caracteristiques_qualifiantes
            == caracteristiques_2023
        )


def test_actualise_caracteristiques(entreprise_non_qualifiee):
    assert entreprise_non_qualifiee.caracteristiques_actuelles() is None

    effectif = CaracteristiquesAnnuelles.EFFECTIF_ENTRE_300_ET_499
    effectif_outre_mer = CaracteristiquesAnnuelles.EFFECTIF_OUTRE_MER_MOINS_DE_250
    effectif_groupe = CaracteristiquesAnnuelles.EFFECTIF_MOINS_DE_50
    tranche_chiffre_affaires = CaracteristiquesAnnuelles.CA_MOINS_DE_700K
    tranche_bilan = CaracteristiquesAnnuelles.BILAN_MOINS_DE_350K
    tranche_chiffre_affaires_consolide = CaracteristiquesAnnuelles.CA_MOINS_DE_700K
    tranche_bilan_consolide = CaracteristiquesAnnuelles.BILAN_MOINS_DE_350K
    bdese_accord = False
    systeme_management_energie = False
    date_cloture_exercice = date(2023, 7, 7)

    actualisation = ActualisationCaracteristiquesAnnuelles(
        date_cloture_exercice,
        effectif,
        effectif_outre_mer,
        effectif_groupe,
        tranche_chiffre_affaires,
        tranche_bilan,
        tranche_chiffre_affaires_consolide,
        tranche_bilan_consolide,
        bdese_accord,
        systeme_management_energie,
    )
    caracteristiques = entreprise_non_qualifiee.actualise_caracteristiques(
        actualisation
    )
    caracteristiques.save()

    caracteristiques = CaracteristiquesAnnuelles.objects.get(pk=caracteristiques.pk)
    assert caracteristiques.annee == 2023
    assert caracteristiques.effectif == effectif
    assert caracteristiques.effectif_outre_mer == effectif_outre_mer
    assert caracteristiques.effectif_groupe == effectif_groupe
    assert caracteristiques.tranche_chiffre_affaires == tranche_chiffre_affaires
    assert caracteristiques.tranche_bilan == tranche_bilan
    assert (
        caracteristiques.tranche_chiffre_affaires_consolide
        == tranche_chiffre_affaires_consolide
    )
    assert caracteristiques.tranche_bilan_consolide == tranche_bilan_consolide
    assert caracteristiques.bdese_accord == bdese_accord
    assert caracteristiques.systeme_management_energie == systeme_management_energie
    entreprise_non_qualifiee.refresh_from_db()
    assert entreprise_non_qualifiee.caracteristiques_annuelles(2023) == caracteristiques

    nouvel_effectif = CaracteristiquesAnnuelles.EFFECTIF_ENTRE_500_ET_4999
    nouvel_effectif_outre_mer = CaracteristiquesAnnuelles.EFFECTIF_OUTRE_MER_250_ET_PLUS
    nouvel_effectif_groupe = CaracteristiquesAnnuelles.EFFECTIF_ENTRE_500_ET_4999
    nouvelle_tranche_chiffre_affaires = CaracteristiquesAnnuelles.CA_ENTRE_700K_ET_12M
    nouvelle_tranche_bilan = CaracteristiquesAnnuelles.BILAN_ENTRE_6M_ET_20M
    nouvelle_tranche_chiffre_affaires_consolide = (
        CaracteristiquesAnnuelles.CA_ENTRE_700K_ET_12M
    )
    nouvelle_tranche_bilan_consolide = CaracteristiquesAnnuelles.BILAN_ENTRE_6M_ET_20M
    nouveau_bdese_accord = True
    nouveau_systeme_management_energie = True

    actualisation = ActualisationCaracteristiquesAnnuelles(
        date_cloture_exercice,
        nouvel_effectif,
        nouvel_effectif_outre_mer,
        nouvel_effectif_groupe,
        nouvelle_tranche_chiffre_affaires,
        nouvelle_tranche_bilan,
        nouvelle_tranche_chiffre_affaires_consolide,
        nouvelle_tranche_bilan_consolide,
        nouveau_bdese_accord,
        nouveau_systeme_management_energie,
    )
    nouvelles_caracteristiques = entreprise_non_qualifiee.actualise_caracteristiques(
        actualisation
    )
    nouvelles_caracteristiques.save()

    nouvelles_caracteristiques = CaracteristiquesAnnuelles.objects.get(
        pk=nouvelles_caracteristiques.pk
    )
    assert nouvelles_caracteristiques.effectif == nouvel_effectif
    assert nouvelles_caracteristiques.effectif_outre_mer == nouvel_effectif_outre_mer
    assert nouvelles_caracteristiques.effectif_groupe == nouvel_effectif_groupe
    assert (
        nouvelles_caracteristiques.tranche_chiffre_affaires
        == nouvelle_tranche_chiffre_affaires
    )
    assert nouvelles_caracteristiques.tranche_bilan == nouvelle_tranche_bilan
    assert (
        nouvelles_caracteristiques.tranche_chiffre_affaires_consolide
        == nouvelle_tranche_chiffre_affaires_consolide
    )
    assert (
        nouvelles_caracteristiques.tranche_bilan_consolide
        == nouvelle_tranche_bilan_consolide
    )
    assert nouvelles_caracteristiques.bdese_accord == nouveau_bdese_accord
    assert (
        nouvelles_caracteristiques.systeme_management_energie
        == nouveau_systeme_management_energie
    )
    entreprise_non_qualifiee.refresh_from_db()
    assert (
        entreprise_non_qualifiee.caracteristiques_annuelles(2023)
        == nouvelles_caracteristiques
    )


@pytest.mark.django_db(transaction=True)
def test_caracteristiques_annuelles(entreprise_non_qualifiee):
    with pytest.raises(IntegrityError):
        CaracteristiquesAnnuelles.objects.create(annee=2023)

    CaracteristiquesAnnuelles.objects.create(
        entreprise=entreprise_non_qualifiee, annee=2023
    )


def test_uniques_caracteristiques_annuelles(entreprise_non_qualifiee):
    caracteristiques = CaracteristiquesAnnuelles(
        entreprise=entreprise_non_qualifiee, annee=2023
    )
    caracteristiques.save()

    with pytest.raises(IntegrityError):
        caracteristiques_bis = CaracteristiquesAnnuelles(
            entreprise=entreprise_non_qualifiee, annee=2023
        )
        caracteristiques_bis.save()


def test_caracteristiques_actuelles_selon_la_date_de_cloture(entreprise_non_qualifiee):
    entreprise_non_qualifiee.date_cloture_exercice = date(2000, 6, 30)
    for annee in (2022, 2023):
        actualisation = ActualisationCaracteristiquesAnnuelles(
            date(annee, 6, 30),
            effectif=CaracteristiquesAnnuelles.EFFECTIF_10000_ET_PLUS,
            effectif_outre_mer=CaracteristiquesAnnuelles.EFFECTIF_OUTRE_MER_250_ET_PLUS,
            effectif_groupe=None,
            tranche_chiffre_affaires=CaracteristiquesAnnuelles.CA_MOINS_DE_700K,
            tranche_bilan=CaracteristiquesAnnuelles.BILAN_100M_ET_PLUS,
            tranche_chiffre_affaires_consolide=None,
            tranche_bilan_consolide=None,
            bdese_accord=False,
            systeme_management_energie=False,
        )
        caracs = entreprise_non_qualifiee.actualise_caracteristiques(actualisation)
        caracs.save()

    with freeze_time(datetime(2023, 1, 27, 16, 1, tzinfo=timezone.utc)):
        assert entreprise_non_qualifiee.caracteristiques_actuelles().annee == 2022

    with freeze_time(datetime(2023, 11, 27, 16, 1, tzinfo=timezone.utc)):
        assert entreprise_non_qualifiee.caracteristiques_actuelles().annee == 2023

    with freeze_time(datetime(2024, 11, 27, 16, 1, tzinfo=timezone.utc)):
        assert entreprise_non_qualifiee.caracteristiques_actuelles() is None


def test_categorie_SA():
    for cat_insee in (
        5505,  # SA à participation ouvrière à conseil d'administration
        5699,  # SA à directoire (s.a.i.)
    ):
        assert categorie(cat_insee) == CategorieJuridique.SOCIETE_ANONYME


def test_categorie_SCA():
    for cat_insee in (
        5308,  # Société en commandite par actions
        5385,  # Société d'exercice libéral en commandite par actions
    ):
        assert categorie(cat_insee) == CategorieJuridique.SOCIETE_COMMANDITE_PAR_ACTION


def test_categorie_SAS():
    for cat_insee in (
        5710,  # SAS, société par actions simplifiée
        5785,  # Société d'exercice libéral par action simplifiée
    ):
        assert categorie(cat_insee) == CategorieJuridique.SOCIETE_PAR_ACTION_SIMPLIFIEE


def test_categorie_SE():
    assert categorie(5800) == CategorieJuridique.SOCIETE_EUROPEENNE


def test_categorie_non_traitee():
    cat_insee = 9240  # congrégation
    assert categorie(cat_insee) is None
