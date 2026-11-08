from django import forms

from .models import paiement


class PaiementForm(forms.ModelForm):
    class Meta:
        model = paiement
        fields = ["eleve_nom", "prix", "mode_paiement", "statut"]
        labels = {
            "eleve_nom": "Nom complet de l'etudiant",
            "prix": "Montant (FCFA)",
            "mode_paiement": "Mode de paiement",
            "statut": "Statut",
        }
        widgets = {
            "eleve_nom": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex. Awa Diop",
                "autocomplete": "name",
            }),
            "prix": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Ex. 25000",
                "min": "0.01",
                "step": "0.01",
            }),
            "mode_paiement": forms.Select(attrs={"class": "form-control"}),
            "statut": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_eleve_nom(self):
        return self.cleaned_data["eleve_nom"].strip()
