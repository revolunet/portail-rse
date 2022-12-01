# Generated by Django 4.1.2 on 2022-12-01 14:12

from django.db import migrations, models
import django.forms.fields
import reglementations.models


class Migration(migrations.Migration):

    dependencies = [
        (
            "reglementations",
            "0012_bdese_300_nombre_examens_medicaux_complementaires_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bdese_300",
            name="remuneration_moyenne_femme",
        ),
        migrations.RemoveField(
            model_name="bdese_300",
            name="remuneration_moyenne_homme",
        ),
        migrations.RemoveField(
            model_name="bdese_300",
            name="remuneration_moyenne_par_age_femme",
        ),
        migrations.RemoveField(
            model_name="bdese_300",
            name="remuneration_moyenne_par_age_homme",
        ),
        migrations.AddField(
            model_name="bdese_300",
            name="remuneration_femme",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                null=True,
                verbose_name="Rémunération moyenne/médiane mensuelle des femmes par catégorie professionnelle",
            ),
        ),
        migrations.AddField(
            model_name="bdese_300",
            name="remuneration_homme",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                null=True,
                verbose_name="Rémunération moyenne/médiane mensuelle des hommes par catégorie professionnelle",
            ),
        ),
        migrations.AddField(
            model_name="bdese_300",
            name="remuneration_moyenne_ou_mediane",
            field=models.CharField(
                choices=[
                    ("moyenne", "Rémunération moyenne"),
                    ("mediane", "Rémunération médiane"),
                ],
                default="moyenne",
                help_text="Les indicateurs suivants peuvent être renseignés au choix en rémunération moyenne ou rémunération médiane",
                max_length=10,
                verbose_name="Rémunération moyenne ou médiane",
            ),
        ),
        migrations.AddField(
            model_name="bdese_300",
            name="remuneration_par_age_femme",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=[
                    "moins de 30 ans",
                    "30 à 39 ans",
                    "40 à 49 ans",
                    "50 ans et plus",
                ],
                null=True,
                verbose_name="Rémunération moyenne/médiane mensuelle des femmes par tranche d'âge",
            ),
        ),
        migrations.AddField(
            model_name="bdese_300",
            name="remuneration_par_age_homme",
            field=reglementations.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=[
                    "moins de 30 ans",
                    "30 à 39 ans",
                    "40 à 49 ans",
                    "50 ans et plus",
                ],
                null=True,
                verbose_name="Rémunération moyenne/mediane mensuelle des hommes par tranche d'âge",
            ),
        ),
    ]
