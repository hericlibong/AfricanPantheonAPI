# Generated by Django 5.0.6 on 2024-06-25 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entities", "0008_mythicalcreature_appareance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mythicalcreature",
            name="appareance",
            field=models.TextField(
                blank=True,
                help_text="Brêve description de la créature. Mise en avant de ses attributs physiques",
                null=True,
            ),
        ),
    ]
