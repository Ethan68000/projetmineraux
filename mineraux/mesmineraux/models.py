from django.db import models

class mesmineraux(models.Model):
    nompierre = models.CharField(max_length=100)
    couleur = models.CharField(max_length = 100)
    nationalité = models.CharField(max_length = 100)
    poids = models.IntegerField(blank=False)
    resume = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.nompierre} de couleur {self.couleur} qui vient de {self.nationalité} et qui pèse {self.poids} kg"
        return chaine
    def dic(self):
        return {"nompierre":self.nompierre, "couleur":self.couleur, "nationalité":self.nationalité, "poids":self.poids,}

class Livre(models.Model):
    nom_livre = models.CharField(max_length=100)
    contenu_pierre = models.CharField(max_length=100)
    page = models.IntegerField(blank=False)
    resume = models.CharField(max_length=500)
    mesmineraux = models.ForeignKey("mesmineraux", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chainelivre = f"{self.nom_livre} qui contient les pierres {self.contenu_pierre} qui fait {self.page} page et qui parle de {self.resume} avec la pierre {self.mesmineraux}"
        return chainelivre

    def dic(self):
        return {"nom_livre":self.nom_livre, "conten_pierre":self.contenu_pierre, "page":self.page, "resume":self.resume, "mesmineraux":self.mesmineraux}