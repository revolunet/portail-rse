from datetime import datetime

import pytest
from django.core.exceptions import ValidationError

from ..models import RapportCSRD
from reglementations.enums import ENJEUX_NORMALISES

# Fixtures :
# voir pour pull-up éventuel, au besoin


@pytest.fixture
def rapport_personnel(alice, entreprise_non_qualifiee):
    return RapportCSRD.objects.create(
        proprietaire=alice,
        entreprise=entreprise_non_qualifiee,
        annee=f"{datetime.now():%Y}",
    )


def test_clean_rapport_csrd(rapport_personnel):
    # `clean()` contient quelques vérifications pour voir si un modèle est personnel ou principal
    assert not rapport_personnel.is_principal()

    # clean doit être sans effet
    rapport_personnel.clean()

    # modification en principal
    alice = rapport_personnel.proprietaire
    rapport_personnel.proprietaire = None
    rapport_personnel.save()

    assert (
        rapport_personnel.is_principal
    ), "le rapport CSRD doit être principal (sans propriétaire)"

    # passage en personnel après avoir été principal : non
    rapport_personnel.proprietaire = alice
    with pytest.raises(
        ValidationError,
        match="Impossible de modifier le rapport CSRD principal en rapport personnel",
    ):
        rapport_personnel.clean()

    # enregistrement d'un nouveau rapport principal : non
    rapport_personnel.pk = None
    rapport_personnel.proprietaire = None
    with pytest.raises(
        ValidationError,
        match="Il existe déjà un rapport CSRD principal pour cette entreprise",
    ):
        rapport_personnel.clean()


def test_enjeux_normalises_presents(rapport_personnel):
    # les enjeux normalisés doivent être présents sur un nouveau rapport CSRD

    # FIXME : plante et c'est normal, l'ordonnancement est à revoir :)

    for idx, enjeu_normalise in enumerate(ENJEUX_NORMALISES):
        enjeu = rapport_personnel.enjeux.order_by("ordre")[idx]
        nom, esrs, description = enjeu.nom, enjeu.esrs, enjeu.description
        assert (nom, esrs, description) == (
            enjeu_normalise.nom,
            enjeu_normalise.esrs,
            enjeu_normalise.description,
        )
