# Generated by Django 4.2.2 on 2023-06-12 16:23
import django.utils.timezone
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("entreprises", "0018_remove_entreprise_bdese_accord_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="evolution",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="evolution",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
