# Generated by Django 4.2 on 2023-06-21 09:11
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("metabase", "0004_rename_raison_sociale_entreprise_denomination"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entreprise",
            name="bdese_accord",
            field=models.BooleanField(null=True),
        ),
    ]
