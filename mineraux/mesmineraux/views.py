from django.http import HttpResponseRedirect
from .forms import mesminerauxForm
from django.shortcuts import render
from . import models


def index(request):
    liste = models.mesmineraux.objects.all()
    return render(request, 'mesmineraux/index.html', {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = mesminerauxForm(request)
        if form.is_valid():
            mesmineraux = form.save()
            return render(request,"mesmineraux/affiche.html",{"mesmineraux" : mesmineraux})
        else:
            return render(request,"mesmineraux/ajout.html",{"form": form})
    else :
        form = mesminerauxForm()
        return render(request,"mesmineraux/ajout.html",{"form" : form})

def traitement(request):
    lform = mesminerauxForm(request.POST)
    if lform.is_valid():
        mesmineraux = lform.save()
        return render(request, "mesmineraux/affiche.html", {"mesmineraux": mesmineraux})
    else:
        return render(request, "mesmineraux/ajout.html", {"form": lform})
    
def affiche(request, id):
    mesmineraux = models.mesmineraux.objects.get(pk=id)
    return render(request, "mesmineraux/affiche.html",{"mesmineraux": mesmineraux})

def delete(request, id):
    suppr = models.mesmineraux.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/mesmineraux/index/",)

def update(request, id):
    pierre = models.mesmineraux.objects.get(pk=id)
    aform = mesminerauxForm(pierre.dic())
    return render(request, "mesmineraux/ajoutupdate.html/", {"form":aform, "id":id})


def updatetraitement(request, id):
    aform = mesminerauxForm(request.POST)
    saveid = id
    if aform.is_valid():
        mesmineraux = aform.save(commit = False)
        mesmineraux.id = saveid
        mesmineraux.save()
        return HttpResponseRedirect("/mesmineraux/index/")
    else:
        return render(request, "mesmineraux/ajoutupdate.html", {"form": aform})