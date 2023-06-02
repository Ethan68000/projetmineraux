from django.db import models

class Pierre(models.Model):
    nompierre = models.CharField(max_length=100)
    couleur = models.CharField(max_length = 100)
    nationalité = models.CharField(max_length = 100)
    poids = models.IntegerField(blank=False)
    resume = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.nompierre} de couleur {self.couleur} qui vient de {self.nationalité} et qui pèse {self.poids} kg"
        return chaine

class Livre(models.Model):
    nom_livre = models.CharField(max_length=100)
    contenu_pierre = models.CharField(max_length=100)
    page = models.IntegerField(blank=False)
    resume = models.CharField(max_length=500)