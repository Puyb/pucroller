# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0003_auto_20170911_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licences2016',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('num_licence', models.CharField(verbose_name='Numéro de licence', max_length=15, blank=True, help_text='Si vous le connaissez')),
            ],
        ),
    ]
