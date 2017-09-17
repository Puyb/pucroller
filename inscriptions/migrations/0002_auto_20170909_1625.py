# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membre',
            old_name='code',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='membre',
            name='chomeur_etudiant',
            field=models.BooleanField(verbose_name='Je suis chomeur ou étudiant'),
        ),
        migrations.AlterField(
            model_name='membre',
            name='contact_nom',
            field=models.CharField(verbose_name='Nom', max_length=200, help_text='Personne a contacter en cas de problème ou responsable légale pour un mineur'),
        ),
        migrations.AlterField(
            model_name='membre',
            name='contact_telephone',
            field=models.CharField(verbose_name='Téléphone', max_length=200),
        ),
        migrations.AlterField(
            model_name='membre',
            name='email',
            field=models.EmailField(verbose_name='e-mail', max_length=200),
        ),
        migrations.AlterField(
            model_name='membre',
            name='photo',
            field=models.FileField(verbose_name="Photo d'identité", blank=True, help_text='Si vous le pouvez, ajoutez la photo (formats JPEG). ', upload_to='certificats'),
        ),
    ]
