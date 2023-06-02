from django.urls import path
from . import views
from . import livreviews

urlpatterns = [
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('panier/<int:id>/', views.panier),
    path('delete/<int:id>/', views.delete),

    #path('indexlivre/', livreviews.index),
    path('ajoutlivre/', livreviews.ajout),
    #path('traitementlivre/', livreviews.traitement),
    #path('affichelivre/<int:id>/', livreviews.affiche),
    #path('deletelivre/<int:id>/', livreviews.delete)

]
