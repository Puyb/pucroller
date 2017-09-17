# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0005_auto_20170916_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='membre',
            name='autre_club',
            field=models.BooleanField(verbose_name="J'ai une licence dans un autre club et je souhaite rester licencié dans ce club.", default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cours',
            name='discipline',
            field=models.CharField(verbose_name='Discipline', max_length=20, choices=[('rando init', 'Randonnée initiation'), ('Roller Freestyle', 'Slalom'), ('Course', 'Course')]),
        ),
        migrations.AlterField(
            model_name='membre',
            name='cours',
            field=models.ManyToManyField(verbose_name='Sessions', help_text="Cochez la ou les sessions auxquelles vous souhaitez participer. Cette selection n'est pas définitive. Vous pouvez changer d'avis en cours d'année...", to='inscriptions.Cours'),
        ),
        migrations.AlterField(
            model_name='membre',
            name='discipline',
            field=models.CharField(verbose_name='Discipline', max_length=20, choices=[('rando init', 'Randonnée initiation'), ('Roller Freestyle', 'Slalom'), ('Course', 'Course')]),
        ),
        migrations.AlterField(
            model_name='membre',
            name='password',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='membre',
            name='prix',
            field=models.DecimalField(verbose_name='Prix', default=Decimal('0'), max_digits=5, decimal_places=2),
        ),
    ]
