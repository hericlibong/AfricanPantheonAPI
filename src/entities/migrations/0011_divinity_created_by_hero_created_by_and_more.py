# Generated by Django 5.0.6 on 2024-07-14 19:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0010_alter_hero_country'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='divinity',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Utilisateur qui a créé la divinité.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_divinities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hero',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Utilisateur qui a créé le héros.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_heroes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mythicalcreature',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Utilisateur qui a créé la créature.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_creatures', to=settings.AUTH_USER_MODEL),
        ),
    ]