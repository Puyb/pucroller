# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0002_auto_20170909_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membre',
            name='chomeur_etudiant',
        ),
        migrations.AddField(
            model_name='membre',
            name='reduction',
            field=models.CharField(verbose_name='Réduction', max_length=20, default='actif', choices=[('actif', 'Actif ou retraité'), ('enfant', 'Enfant'), ('etudiant', 'Etudiant'), ('chommeur', 'Chomeur')]),
        ),
        migrations.AlterField(
            model_name='membre',
            name='certificat',
            field=models.FileField(verbose_name='Certificat médical', blank=True, help_text='Votre certificat médical doit dater de moins de 1 ans et doit mentionner que vous êtes "aptes à la pratique du roller" et "en compétition" si vous souhaitez faire des compétitions. Si vous le pouvez, scannez le certificat et ajoutez le (formats PDF ou JPEG). ', upload_to='certificats'),
        ),
        migrations.AlterField(
            model_name='membre',
            name='cours',
            field=models.ManyToManyField(verbose_name='Session', help_text="Cochez le ou les sessions auxquelles vous souhaitez participer. Cette selection n'est pas définitive. Vous pouvez changer d'avis en cours d'année...", to='inscriptions.Cours'),
        ),
        migrations.AlterField(
            model_name='membre',
            name='num_licence',
            field=models.CharField(verbose_name='Numéro de licence', max_length=15, blank=True, help_text='Si vous le connaissez'),
        ),
    ]
