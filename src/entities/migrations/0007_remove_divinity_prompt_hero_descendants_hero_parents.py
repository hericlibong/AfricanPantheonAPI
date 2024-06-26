# Generated by Django 5.0.6 on 2024-06-25 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entities", "0006_hero_achievements_hero_allies_hero_enemies_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="divinity",
            name="prompt",
        ),
        migrations.AddField(
            model_name="hero",
            name="descendants",
            field=models.CharField(
                blank=True,
                help_text="Noms des descendants de du héros, si descendants connus.",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="hero",
            name="parents",
            field=models.CharField(
                blank=True,
                help_text="Nom des parents du héros ou parents connus.",
                max_length=255,
                null=True,
            ),
        ),
    ]