from django.contrib import admin
from .models import paiement


@admin.register(paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ("id", "eleve_nom", "prix", "mode_paiement", "statut", "heure")
    list_filter = ("statut", "mode_paiement", "heure")
    search_fields = ("eleve_nom",)
    readonly_fields = ("heure",)
# Register your models here.
