from django.urls import path

from . import views

app_name = "entreprises"
urlpatterns = [
    path("entreprises", views.index, name="entreprises"),
    path("entreprises/<str:siren>", views.qualification, name="qualification"),
]
