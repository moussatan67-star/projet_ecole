from django.core.validators import MinValueValidator
from django.db import models


class paiement(models.Model):
    MODE_CHOICES = [
        ("especes", "Especes"),
        ("carte", "Carte bancaire"),
        ("wave", "Wave / mobile money"),
        ("virement", "Virement bancaire"),
    ]
    STATUT_CHOICES = [
        ("paye", "Paye"),
        ("en_attente", "En attente"),
    ]

    eleve_nom = models.CharField(max_length=150)
    prix = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )
    heure = models.DateTimeField(auto_now_add=True)
    mode_paiement = models.CharField(max_length=20, choices=MODE_CHOICES)
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default="paye",
    )

    class Meta:
        ordering = ["-heure", "-id"]
        verbose_name = "paiement"
        verbose_name_plural = "paiements"

    def __str__(self):
        return f"Paiement #{self.pk or 'nouveau'} - {self.eleve_nom} - {self.prix} FCFA"
