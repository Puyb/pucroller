# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0008_membre_inscrit_ffrs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membre',
            old_name='inscrit_ffrs',
            new_name='licence',
        ),
    ]
