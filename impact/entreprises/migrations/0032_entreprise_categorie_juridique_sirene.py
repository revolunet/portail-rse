# Generated by Django 4.2.1 on 2023-07-19 14:01
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("entreprises", "0031_caracteristiquesannuelles_effectif_groupe_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="entreprise",
            name="categorie_juridique_sirene",
            field=models.IntegerField(null=True),
        ),
    ]
