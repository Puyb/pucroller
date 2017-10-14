from datetime import datetime
from django.forms import ModelForm, Select, RadioSelect, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _
from .models import Membre, Cours, SEXE_CHOICES, REDUCTION_CHOICES, COURS_HELP

class MembreForm(ModelForm):
    class Meta:
        model = Membre
        exclude = ('saison', 'certificat_valide', 'paiement', 'paiement_info', 'date', 'password', 'certificat_valide', 'photo_valide', 'prix', 'licence')
        widgets = {
            'sexe':              Select(choices=SEXE_CHOICES),
            'reduction':         RadioSelect(choices=REDUCTION_CHOICES),
            'date_de_naissance': SelectDateWidget(years=range(datetime.now().year , datetime.now().year - 100, -1)),
        }

    cours = ModelMultipleChoiceField(
        queryset=Cours.objects.all(),
        widget=CheckboxSelectMultiple,
        label='Sessions',
        help_text=COURS_HELP,
    )
        
    def __init__(self, *args, saison=None, **kwargs):
        self._saison = saison
        super().__init__(*args, **kwargs)
        #self.fields['cours'].widget.attrs['class'] = 'selectpicker'
        self.fields['cours'].queryset = Cours.objects.filter(saison=self._saison)

