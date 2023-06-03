from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import livreForm
from . import models

def ajout(request):
    if request.method == "POST":
        form = livreForm(request)
        if form.is_valid():
            livre = form.save()
            return render(request,"livre/affiche.html",{"livre" : livre})
        else:
            return render(request,"livre/ajout.html",{"form": form})
    else :
        form = livreForm()
        return render(request,"livre/ajout.html",{"form" : form})


def traitement(request):
    lform = livreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request, "livre/affiche.html", {"livre": livre})
    else:
        return render(request, "livre/ajout.html", {"form": lform})


def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request, "livre/affiche.html", {"livre": livre})

def delete(request, id):
    suppr = models.Livre.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/mesmineraux/indexlivre/",)

def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    aform = livreForm(livre.dic())
    return render(request, "livre/ajoutupdate.html/", {"form":aform, "id":id})


def updatetraitement(request, id):
    aform = livreForm(request.POST)
    saveid = id
    if aform.is_valid():
        livre = aform.save(commit = False)
        livre.id = saveid
        livre.save()
        return HttpResponseRedirect("/mesmineraux/indexlivre/")
    else:
        return render(request, "livre/ajoutupdate.html", {"form": aform})

def index(request):
    liste = models.Livre.objects.all()
    return render(request, 'livre/index.html', {"liste": liste})