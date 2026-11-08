from django.urls import path
from . import views

app_name = 'paiement'

urlpatterns = [
    path("", views.list_paiement, name="list_paiement"),
    path("nouveau/", views.ajouter_paiement, name="ajouter_paiement"),
    path("<int:pk>/recu/", views.recu_paiement, name="recu"),
]