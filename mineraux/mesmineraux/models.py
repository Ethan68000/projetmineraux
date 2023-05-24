from django.db import models

class Livre(models.Model):
    nompierre = models.CharField(max_length=100)
    couleur = models.CharField(max_length = 100)
    nationalité = models.CharField(max_length = 100)
    poids = models.IntegerField(blank=False)
    resume = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.titre} écrit par {self.auteur} édité le {self.date_parution}"
        return chaine