from django.shortcuts import render
from .forms import LivreForm
from . import models

def index(request):
    return render(request, 'mesmineraux/index.html')

def formulaire(request):
    return render(request,'mesmineraux/formulaire.html')

def main(request):
    return render(request, 'mesmineraux/main.html')

def bonjour(request):
    nom=request.GET["nom"]
    return render(request,'mesmineraux/bonjour.html',{"nom":nom})

def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            livre = form.save()
            return render(request,"mesmineraux/affiche.html",{"livre" : livre})
        else:
            return render(request,"mesmineraux/ajout.html",{"form": form})
    else :
        form = LivreForm()
        return render(request,"mesmineraux/ajout.html",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request, "mesmineraux/affiche.html", {"livre": livre})
    else:
        return render(request, "mesmineraux/ajout.html", {"form": lform})
    
def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request,"mesmineraux/affiche.html",{"livre": livre})
