from django.http import HttpResponseRedirect
from .forms import PierreForm
from django.shortcuts import render
from . import models


def index(request):
    liste = models.Pierre.objects.all()
    return render(request, 'mesmineraux/index.html', {"liste": liste})

def ajout(request):
    if request.method == "POST":
        form = PierreForm(request)
        if form.is_valid():
            pierre = form.save()
            return render(request,"mesmineraux/affiche.html",{"pierre" : pierre})
        else:
            return render(request,"mesmineraux/ajout.html",{"form": form})
    else :
        form = PierreForm()
        return render(request,"mesmineraux/ajout.html",{"form" : form})

def traitement(request):
    lform = PierreForm(request.POST)
    if lform.is_valid():
        pierre = lform.save()
        return render(request, "mesmineraux/affiche.html", {"pierre": pierre})
    else:
        return render(request, "mesmineraux/ajout.html", {"form": lform})
    
def affiche(request, id):
    pierre = models.Pierre.objects.get(pk=id)
    return render(request, "mesmineraux/affiche.html",{"pierre": pierre})

def delete(request, id):
    suppr = models.Pierre.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/mesmineraux/index/",)

def update(request, id):
    pierre = models.Pierre.objects.get(pk=id)
    aform = PierreForm(pierre.dic())
    return render(request, "mesmineraux/ajoutupdate.html/", {"form":aform, "id":id})


def updatetraitement(request, id):
    aform = PierreForm(request.POST)
    saveid = id
    if aform.is_valid():
        pierre = aform.save(commit = False)
        pierre.id = saveid
        pierre.save()
        return HttpResponseRedirect("/mesmineraux/index/")
    else:
        return render(request, "mesmineraux/ajoutupdate.html", {"form": aform})