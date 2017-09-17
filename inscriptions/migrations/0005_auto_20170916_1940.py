# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0004_licences2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saison',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('annee', models.IntegerField()),
                ('ouvert', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Licences2016',
        ),
        migrations.AddField(
            model_name='cours',
            name='saison',
            field=models.ForeignKey(default=1, to='inscriptions.Saison'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membre',
            name='saison',
            field=models.ForeignKey(default=1, to='inscriptions.Saison'),
            preserve_default=False,
        ),
    ]
