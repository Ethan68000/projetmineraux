from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class mesminerauxForm(ModelForm):
    class Meta:
        model = models.mesmineraux
        fields = ('nompierre', 'couleur', 'nationalité', 'poids','resume', 'livre')
        labels = {
            'nompierre' : _('Nom de la pierre'),
            'couleur' : _('Quelle est sa couleur') ,
            'nationalité' : _('quelle est sa provenance'),
            'poids' : _('poids'),
            'description' : _('description'),
            'livre' : _('livre')
        }

class livreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('nom_livre', 'contenu_pierre', 'page', 'resume')
        labels = {
            'nom_livre' : _('Nom du livre'),
            'contenu_pierre' : _('Quel pierre seront dedans'),
            'page' : _('nombre de page'),
            'resume'  : _('Resume du livre'),
        }