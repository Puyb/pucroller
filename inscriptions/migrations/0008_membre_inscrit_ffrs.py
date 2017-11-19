# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0007_auto_20170922_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='membre',
            name='inscrit_ffrs',
            field=models.BooleanField(default=False),
        ),
    ]
