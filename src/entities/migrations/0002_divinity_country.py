# Generated by Django 5.0.6 on 2024-06-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entities", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="divinity",
            name="country",
            field=models.CharField(
                blank=True,
                help_text="Pays actuel d'où est issue la divinité",
                max_length=50,
                null=True,
            ),
        ),
    ]
