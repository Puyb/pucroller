# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nom', models.CharField(verbose_name='Nom', max_length=200)),
                ('lieu', models.CharField(verbose_name='Lieu', max_length=200)),
                ('horaire', models.CharField(verbose_name='Horaire', max_length=200)),
                ('discipline', models.CharField(verbose_name='Discipline', max_length=20, choices=[('rando init', 'Randonnée initiation'), ('slalom', 'Slalom'), ('course', 'Course'), ('hockey', 'Hockey')])),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nom', models.CharField(verbose_name='Nom', max_length=200)),
                ('prenom', models.CharField(verbose_name='Prénom', max_length=200, blank=True)),
                ('sexe', models.CharField(verbose_name='Sexe', max_length=1, choices=[('H', 'Homme'), ('F', 'Femme')])),
                ('adresse1', models.CharField(verbose_name='Adresse', max_length=200, blank=True)),
                ('adresse2', models.CharField(verbose_name='Adresse', max_length=200, blank=True)),
                ('ville', models.CharField(max_length=200)),
                ('code_postal', models.CharField(max_length=200)),
                ('email', models.EmailField(verbose_name='e-mail', max_length=200, blank=True)),
                ('telephone', models.CharField(max_length=200)),
                ('date_de_naissance', models.DateField(verbose_name='Date de naissance')),
                ('chomeur_etudiant', models.BooleanField()),
                ('num_licence', models.CharField(verbose_name='Numéro de licence', max_length=15, blank=True)),
                ('discipline', models.CharField(verbose_name='Discipline', max_length=20, choices=[('rando init', 'Randonnée initiation'), ('slalom', 'Slalom'), ('course', 'Course'), ('hockey', 'Hockey')])),
                ('certificat', models.FileField(verbose_name='Certificat', blank=True, help_text='Si vous le pouvez, scannez le certificat et ajoutez le (formats PDF ou JPEG). ', upload_to='certificats')),
                ('certificat_valide', models.NullBooleanField(verbose_name='Certificat valide')),
                ('photo', models.FileField(verbose_name='Certificat', blank=True, help_text='Si vous le pouvez, ajoutez la photo (formats JPEG). ', upload_to='certificats')),
                ('photo_valide', models.NullBooleanField(verbose_name='Certificat valide')),
                ('taille_tshirt', models.CharField(verbose_name='Taille T-shirt', max_length=3, blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')])),
                ('contact_nom', models.CharField(verbose_name='Nom', max_length=200)),
                ('contact_telephone', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(verbose_name='e-mail', max_length=200, blank=True)),
                ('code', models.CharField(max_length=200)),
                ('paiement_info', models.CharField(verbose_name='Détails', max_length=200, blank=True)),
                ('prix', models.DecimalField(verbose_name='Prix', max_digits=5, decimal_places=2)),
                ('paiement', models.DecimalField(verbose_name='Paiement reçu', blank=True, null=True, max_digits=5, decimal_places=2)),
                ('date', models.DateTimeField(verbose_name="Date d'insciption", auto_now_add=True)),
                ('cours', models.ManyToManyField(to='inscriptions.Cours')),
            ],
        ),
    ]
