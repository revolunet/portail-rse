from django.urls import path

from . import views

app_name = "api_interne"
urlpatterns = [
    path("analyse-double-materialite/<str:id>", views.analyse_double_materialite),
    path("search-entreprise/<str:siren>", views.search_entreprise),
]
