# Generated by Django 4.2.2 on 2023-07-04 13:08
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("entreprises", "0024_caracteristiquesannuelles_bilan_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="caracteristiquesannuelles",
            name="systeme_management_energie",
            field=models.BooleanField(
                null=True,
                verbose_name="L'entreprise a mis en place un\xa0<a target='_blank' href='https://agirpourlatransition.ademe.fr/entreprises/demarche-decarbonation-industrie/agir/structurer-demarche/mettre-en-place-systeme-management-energie'>système de management de l’énergie</a>",
            ),
        ),
    ]
