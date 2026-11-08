PROF =[
 {"id": 1, "first_name": "Awa", "last_name": "Diop",
 "classe": "L1", "active": True},
 {"id": 2, "first_name": "Moussa", "last_name": "Fall",
 "classe": "L2", "active": True},
 {"id": 3, "first_name": "Fatou", "last_name": "Ndiaye",
 "classe": "L1", "inative": True},
 {"id": 4, "first_name": "Ibrahima", "last_name": "Sow",
 "classe": "L3", "active": True},

]
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_professeur(request):
    context = {"liste_professeurs": PROF}
    return render (request , "professeur/list_proffesseur.html", context)
