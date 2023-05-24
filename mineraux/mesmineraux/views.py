from django.shortcuts import render

def index(request):
    return render(request, 'mesmineraux/index.html')

def formulaire(request):
    return render(request,'myfirstapp/formulaire.html')