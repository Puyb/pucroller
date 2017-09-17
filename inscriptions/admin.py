# -*- coding: utf-8 -*-
from inscriptions.models import *
from django.contrib import admin


site = admin.site

class SaisonAdmin(admin.ModelAdmin):
    pass
site.register(Saison, SaisonAdmin)

class CoursAdmin(admin.ModelAdmin):
    pass
site.register(Cours, CoursAdmin)

class MembreAdmin(admin.ModelAdmin):
    list_display = ('num_licence', 'nom', 'prenom', 'saison')
site.register(Membre, MembreAdmin)

    
