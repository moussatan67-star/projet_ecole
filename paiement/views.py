from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PaiementForm
from .models import paiement


def list_paiement(request):
    paiements = paiement.objects.all()
    total_encaisse = (
        paiements.filter(statut="paye").aggregate(total=Sum("prix"))["total"] or 0
    )
    return render(
        request,
        "paiement/list_paiement.html",
        {
            "liste_paiements": paiements,
            "total_encaisse": total_encaisse,
        },
    )


def ajouter_paiement(request):
    if request.method == "POST":
        form = PaiementForm(request.POST)
        if form.is_valid():
            paiement_enregistre = form.save()
            messages.success(request, "Le paiement a ete enregistre.")
            return redirect("paiement:recu", pk=paiement_enregistre.pk)
    else:
        form = PaiementForm()

    return render(request, "paiement/ajouter_paiement.html", {"form": form})


def recu_paiement(request, pk):
    paiement_enregistre = get_object_or_404(paiement, pk=pk)
    return render(
        request,
        "paiement/recu_paiement.html",
        {"paiement": paiement_enregistre},
    )
