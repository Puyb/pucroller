# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0009_auto_20171006_2244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cours',
            options={'verbose_name': 'Session'},
        ),
        migrations.AddField(
            model_name='membre',
            name='envoi_puc',
            field=models.DateTimeField(verbose_name='Date envoi au PUC', blank=True, null=True, default=None),
        ),
        migrations.AlterField(
            model_name='membre',
            name='saison',
            field=models.ForeignKey(related_name='membres', to='inscriptions.Saison'),
        ),
    ]
