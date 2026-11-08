ELEVES =[
 {"id": 1, "first_name": "Awa", "last_name": "Diop",
 "classe": "L1", "active": True},
 {"id": 2, "first_name": "Moussa", "last_name": "Fall",
 "classe": "L2", "active": True},
 {"id": 3, "first_name": "Fatou", "last_name": "Ndiaye",
 "classe": "L1", "active": False},
 {"id": 4, "first_name": "Ibrahima", "last_name": "Sow",
 "classe": "L3", "active": True},


]
from django.shortcuts import render
from django.http import Http404

def eleves_detail(request, id):
    for eleves in ELEVES :
        if eleves["id"]== id:
            return render(request, "eleves/eleves_detail.html", {"eleves": eleves})
    raise Http404 ("Etudiants introuvable")


# Create your views here.
def home(request) :
    classes = {eleve["classe"] for eleve in ELEVES}
    total_actifs = sum(1 for eleve in ELEVES if eleve.get("active", False))
    context = {
        "eleves": ELEVES,
        "total_eleves": len(ELEVES),
        "total_actifs": total_actifs,
        "total_inactifs": len(ELEVES) - total_actifs,
        "total_classes": len(classes),
    }
    return render(request , "eleves/acceuil.html", context)