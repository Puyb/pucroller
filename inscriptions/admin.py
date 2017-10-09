# -*- coding: utf-8 -*-
from inscriptions.models import *
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db.models import F, Q
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


site = admin.site

class SaisonAdmin(admin.ModelAdmin):
    pass
site.register(Saison, SaisonAdmin)

class CoursAdmin(admin.ModelAdmin):
    pass
site.register(Cours, CoursAdmin)

class PaiementCompletFilter(SimpleListFilter):
    title = _('Paiement complet')
    parameter_name = 'paiement_complet'
    def lookups(self, request, model_admin):
        return (
            ('paye', _(u'Payé')),
            ('impaye', _(u'Impayé')),
        )
    def queryset(self, request, queryset):
        if self.value() == 'paye':
            return queryset.filter(paiement__gte=F('prix'))
        if self.value() == 'impaye':
            return queryset.filter(Q(paiement__isnull=True) | Q(paiement__lt=F('prix')))
        return queryset

class MembreAdmin(admin.ModelAdmin):
    search_fields = ('num_licence', 'nom', 'prenom', )
    list_display = ('num_licence', 'nom', 'prenom', 'saison', 'date', 'paiement_complet2', 'licence2', 'dossier_complet_auto2')
    list_display_links = ('num_licence', 'nom', 'prenom', )
    list_filter = ['saison', PaiementCompletFilter, 'licence', 'certificat_valide']
    ordering = ['-date', ]

    def paiement_complet2(self, obj):
        return obj.paiement_complet() and u"""<img alt="None" src="/static/admin/img/icon-yes.gif">""" or u"""<img alt="None" src="/static/admin/img/icon-no.gif">"""
    paiement_complet2.allow_tags = True
    paiement_complet2.short_description = '€'
    
    def licence2(self, obj):
        return obj.licence and u"""<img alt="None" src="/static/admin/img/icon-yes.gif">""" or u"""<img alt="None" src="/static/admin/img/icon-no.gif">"""
    licence2.allow_tags = True
    licence2.short_description = 'FFRS'
    
    def dossier_complet_auto2(self, obj):
        if obj.certificat_valide == None:
            return u"""<img alt="None" src="/static/admin/img/icon-unknown.gif">"""
        if obj.certificat_valide == True:
            return u"""<img alt="None" src="/static/admin/img/icon-yes.gif">"""
        if obj.certificat_valide == False:
            return u"""<img alt="None" src="/static/admin/img/icon-no.gif">"""
        return u""
    dossier_complet_auto2.allow_tags = True
    dossier_complet_auto2.short_description = mark_safe(u"""<img alt="None" src="/static/admin/img/icon-yes.gif">""")

site.register(Membre, MembreAdmin)

    
