from django.core.management.base import BaseCommand, CommandError
from inscriptions.models import Saison, Membre
import csv
from datetime import date

class Command(BaseCommand):
    help = 'Import FFRS csv file'

    def add_arguments(self, parser):
        parser.add_argument('saison', type=int)
        parser.add_argument('file')

    def handle(self, *args, **options):
        with open(options['file'], encoding='ISO-8859-15') as csvfile:
            r = csv.DictReader(csvfile, delimiter=';')

            saison = Saison.objects.get(annee=options['saison'])
            for line in r:
                date_array = [int(s) for s in line['Date de naissance'].split('/')]
                date_array.reverse()
                Membre(
                    saison = saison,
                    nom = line['Nom'],
                    prenom = line['Prénom'],
                    sexe = { 'M': 'H', 'F':'F' }[line['Sexe']],
                    adresse1 = line['Adresse 1'],
                    adresse2 = line['Adresse 2'],
                    ville = line['Ville'],
                    code_postal = line['Code postal'],
                    email = line['E-mail'],
                    telephone = line['N° Portable'] or line['N° Tél'],
                    date_de_naissance = date(*date_array),
                    num_licence = line['N° Licencié'],
                    discipline = line['Discipline'],
                    certificat_valide = True,
                    photo_valide = True,
                    taille_tshirt = '',
                    contact_nom = '',
                    contact_telephone = '',
                    contact_email = '',
                ).save()
