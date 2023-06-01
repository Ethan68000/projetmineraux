from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('nompierre', 'couleur', 'nationalité', 'poids','resume')
        labels = {
            'nompierre' : _('Nom de la pierre'),
            'couleur' : _('Quelle est sa couleur') ,
            'nationalité' : _('quelle est sa provenance'),
            'poids' : _('poids'),
            'description' : _('description')
        }