# Generated by Django 4.1.7 on 2023-03-28 15:35
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("metabase", "0003_alter_entreprise_effectif"),
    ]

    operations = [
        migrations.RenameField(
            model_name="entreprise",
            old_name="raison_sociale",
            new_name="denomination",
        ),
    ]
