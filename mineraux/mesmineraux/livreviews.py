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