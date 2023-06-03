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
    def dic(self):
        return {"nompierre":self.nompierre, "couleur":self.couleur, "nationalité":self.nationalité, "poids":self.poids}

class Livre(models.Model):
    nom_livre = models.CharField(max_length=100)
    contenu_pierre = models.CharField(max_length=100)
    page = models.IntegerField(blank=False)
    resume = models.CharField(max_length=500)

    def __str__(self):
        chainelivre = f"{self.nom_livre} qui contient les pierres {self.contenu_pierre} qui fait {self.page} et qui parle de {self.resume}"
        return chainelivre
