# -*- coding: utf-8 -*-
from datetime import date
from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _
import logging

logger = logging.getLogger(__name__)

SEXE_CHOICES = (
    ('H', _(u'Homme')),
    ('F', _(u'Femme')),
)

TAILLES_CHOICES = (
    ('XS', _('XS')),
    ('S', _('S')),
    ('M', _('M')),
    ('L', _('L')),
    ('XL', _('XL')),
    ('XXL', _('XXL')),
)

DISCIPLINE_CHOICES = (
    ('rando init', _('Randonnée initiation')),
    ('Roller Freestyle', _('Slalom')),
    ('Course', _('Course')),
    #('hockey', _('Hockey')),
)

REDUCTION_CHOICES = (
    ('actif', _('Actif ou retraité')),
    ('enfant', _('Enfant')),
    ('etudiant', _('Etudiant')),
    ('chommeur', _('Chomeur')),
)

class Saison(models.Model):
    annee = models.IntegerField()
    ouvert = models.BooleanField()

    def __str__(self):
        return '%s - %s' % (self.annee, self.annee + 1)

class Cours(models.Model):
    saison     = models.ForeignKey(Saison)
    nom        = models.CharField(_(u'Nom'), max_length=200)
    lieu       = models.CharField(_(u'Lieu'), max_length=200)
    horaire    = models.CharField(_(u'Horaire'), max_length=200)
    discipline = models.CharField(_(u'Discipline'), max_length=20, choices=DISCIPLINE_CHOICES)

    def __str__(self):
        return '%s - %s - %s - %s' % (self.nom, self. lieu, self.horaire, self.discipline)

CERTIFICAT_HELP = _("""Votre certificat médical doit dater de moins de 1 ans et doit mentionner que vous êtes "aptes à la pratique du roller" et "en compétition" si vous souhaitez faire des compétitions. Si vous le pouvez, scannez le certificat et ajoutez le (formats PDF ou JPEG). """)
PHOTO_HELP = _("""Si vous le pouvez, ajoutez la photo (formats JPEG). """)
CONTACT_HELP = _("""Personne a contacter en cas de problème ou responsable légale pour un mineur""")
COURS_HELP = _("""Cochez la ou les sessions auxquelles vous souhaitez participer. Cette selection n'est pas définitive. Vous pouvez changer d'avis en cours d'année...""")
LICENCE_HELP = _("""Si vous le connaissez""")

class Membre(models.Model):
    saison            = models.ForeignKey(Saison)
    nom               = models.CharField(_('Nom'), max_length=200)
    prenom            = models.CharField(_('Prénom'), max_length=200, blank=True)
    sexe              = models.CharField(_('Sexe'), max_length=1, choices=SEXE_CHOICES)
    adresse1          = models.CharField(_('Adresse'), max_length=200, blank=True)
    adresse2          = models.CharField(_('Adresse'), max_length=200, blank=True)
    ville             = models.CharField(max_length=200)
    code_postal       = models.CharField(max_length=200)
    email             = models.EmailField(_('e-mail'), max_length=200)
    telephone         = models.CharField(max_length=200)
    date_de_naissance = models.DateField(_('Date de naissance'))
    reduction         = models.CharField(_('Réduction'), max_length=20, default='actif', choices=REDUCTION_CHOICES)
    num_licence       = models.CharField(_('Numéro de licence'), max_length=15, blank=True, help_text=LICENCE_HELP)
    autre_club        = models.BooleanField(_("J'ai une licence dans un autre club et je souhaite rester licencié dans ce club."), default=False)
    discipline        = models.CharField(_('Discipline'), max_length=20, choices=DISCIPLINE_CHOICES)
    cours             = models.ManyToManyField(Cours, verbose_name=_('Sessions'), help_text=COURS_HELP)
    certificat        = models.FileField(_('Certificat médical'), upload_to='certificats', blank=True, help_text=CERTIFICAT_HELP)
    certificat_valide = models.NullBooleanField(_(u'Certificat valide'))
    photo             = models.FileField(_('Photo d\'identité'), upload_to='certificats', blank=True, help_text=PHOTO_HELP)
    photo_valide      = models.NullBooleanField(_(u'Certificat valide'))
    taille_tshirt     = models.CharField(_('Taille T-shirt'), max_length=3, choices=TAILLES_CHOICES, blank=True)
    contact_nom       = models.CharField(_('Nom'), max_length=200, help_text=CONTACT_HELP)
    contact_telephone = models.CharField(_('Téléphone'), max_length=200)
    contact_email     = models.EmailField(_('e-mail'), max_length=200, blank=True)

    password          = models.CharField(max_length=200, blank=True)
    paiement_info     = models.CharField(_('Détails'), max_length=200, blank=True)
    prix              = models.DecimalField(_('Prix'), max_digits=5, decimal_places=2, default=Decimal(0))
    paiement          = models.DecimalField(_('Paiement reçu'), max_digits=5, decimal_places=2, null=True, blank=True)
    date              = models.DateTimeField(_("Date d'insciption"), auto_now_add=True)

    
    def age(self, today=None):
        if not today:
            today = date.today()
        try: 
            birthday = self.date_de_naissance.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = self.date_de_naissance.replace(year=today.year, day=self.date_de_naissance.day-1)
        return today.year - self.date_de_naissance.year - (birthday > today)

    def __str__(self):
        return '%s - %s %s' % (self.num_licence, self.nom, self.prenom)

    def cookie_key(self):
        return 'code_%s' % self.id

