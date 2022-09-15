from django.conf import settings
from django.shortcuts import render
import requests

from .forms import EligibiliteForm, SirenForm


def index(request):
    return render(request, "public/index.html", {"form": SirenForm()})


def siren(request):
    form = SirenForm(request.GET)
    errors = []
    if form.is_valid():
        siren = form.cleaned_data["siren"]

        url = f"https://entreprise.api.gouv.fr/v3/insee/sirene/unites_legales/{siren}"
        headers = {"Authorization": f"Bearer {settings.API_ENTREPRISE_TOKEN}"}
        params = {
            "context": "Test de l'API",
            "object": "Test de l'API",
            "recipient": "10000001700010",
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()["data"]
            raison_sociale = data["personne_morale_attributs"]["raison_sociale"]
            effectif = data["tranche_effectif_salarie"]["a"]
            form = EligibiliteForm()
            return render(
                request,
                "public/siren.html",
                {
                    "siren": siren,
                    "raison_sociale": raison_sociale,
                    "effectif": effectif,
                    "form": form,
                },
            )
        else:
            errors = response.json()["errors"]
    else:
        errors = form.errors

    return render(request, "public/index.html", {"form": form, "errors": errors})


BDESE_ELIGIBILITE = {
    "NON_ELIGIBLE": 0,
    "ELIGIBLE_AVEC_ACCORD": 1,
    "ELIGIBLE_INFERIEUR_300": 2,
    "ELIGIBLE_SUPERIEUR_300": 3,
}


def eligibilite(request):
    form = EligibiliteForm(request.GET)
    if form.is_valid():
        accord = form.cleaned_data["accord"]
        effectif = form.cleaned_data["effectif"]
        if effectif == "petit":
            bdese_result = BDESE_ELIGIBILITE["NON_ELIGIBLE"]
        elif accord:
            bdese_result = BDESE_ELIGIBILITE["ELIGIBLE_AVEC_ACCORD"]
        elif effectif == "moyen":
            bdese_result = BDESE_ELIGIBILITE["ELIGIBLE_INFERIEUR_300"]
        else:
            bdese_result = BDESE_ELIGIBILITE["ELIGIBLE_SUPERIEUR_300"]

    return render(
        request,
        "public/result.html",
        {"BDESE_ELIGIBILITE": BDESE_ELIGIBILITE, "bdese_result": bdese_result},
    )
