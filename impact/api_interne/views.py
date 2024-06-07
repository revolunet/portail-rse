from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


@api_view(["GET", "POST"])
def analyse_double_materialite(request, id):
    json = JSONRenderer().render({"id": id})
    return Response(json)
