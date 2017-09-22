# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0006_auto_20170917_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='autre_club',
            field=models.BooleanField(default=False, verbose_name="J'ai une licence dans un autre club et je souhaite rester licencié dans ce club."),
        ),
        migrations.AlterField(
            model_name='membre',
            name='paiement_info',
            field=models.CharField(max_length=1000, verbose_name='Détails', blank=True),
        ),
        migrations.AlterField(
            model_name='membre',
            name='reduction',
            field=models.CharField(default='actif', max_length=20, choices=[('actif', 'Actif ou retraité'), ('enfant', 'Enfant'), ('etudiant', 'Étudiant'), ('chomeur', 'Chômeur')], verbose_name='Réduction'),
        ),
    ]
