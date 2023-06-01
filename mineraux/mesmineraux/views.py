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

def panier(request, id):
    pierre = models.Pierre.objects.get(pk=id)
    return render(request, "mesmineraux/panier.html", {"pierre": pierre})

def delete(request, id):
    suppr = models.Pierre.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/mesmineraux/index/",)