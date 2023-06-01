from django.http import HttpResponseRedirect
from .forms import LivreForm
from django.shortcuts import render
from . import models


def index(request):
    liste = models.Livre.objects.all()
    return render(request, 'mesmineraux/index.html', {"liste": liste})

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
    return render(request, "mesmineraux/affiche.html",{"livre": livre})

def panier(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request, "mesmineraux/panier.html", {"livre": livre})

def delete(request, id):
    suppr = models.Livre.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/mesmineraux/index/",)