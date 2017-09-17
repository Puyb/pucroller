from datetime import datetime
from django.forms import ModelForm, Select, RadioSelect
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _
from .models import Membre, SEXE_CHOICES, REDUCTION_CHOICES

class MembreForm(ModelForm):
    class Meta:
        model = Membre
        exclude = ('saison', 'certificat_valide', 'paiement', 'paiement_info', 'date', 'password', 'certificat_valide', 'photo_valide', 'prix')
        widgets = {
            'sexe':              Select(choices=SEXE_CHOICES),
            'reduction':         RadioSelect(choices=REDUCTION_CHOICES),
            'date_de_naissance': SelectDateWidget(years=range(datetime.now().year , datetime.now().year - 100, -1)),
        }

        def __init__(self, *args, **kwargs):
            super().__init(*args, **kwargs)
            self.fields['cours'].widget.attrs['class'] = 'selectpicker'

