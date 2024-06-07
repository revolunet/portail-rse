from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

import api.infos_entreprise
from api.exceptions import APIError


@api_view(["GET", "POST"])
def analyse_double_materialite(request, id):
    json = JSONRenderer().render({"id": id})
    return Response(json)


@api_view(["GET"])
def search_entreprise(request, siren):
    try:
        infos = api.infos_entreprise.infos_entreprise(siren, donnees_financieres=True)
    except APIError as exception:
        return JsonResponse(
            {"error": str(exception)},
            status=400,
        )
    return JsonResponse(infos)
