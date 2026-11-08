from decimal import Decimal

from django.test import TestCase, override_settings
from django.urls import reverse

from .models import paiement


@override_settings(ALLOWED_HOSTS=["testserver"])
class PaiementViewsTests(TestCase):
    def test_list_page_renders_empty_state_and_create_link(self):
        response = self.client.get(reverse("paiement:list_paiement"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucun paiement")
        self.assertContains(response, reverse("paiement:ajouter_paiement"))

    def test_valid_payment_is_saved_and_receipt_is_shown(self):
        response = self.client.post(
            reverse("paiement:ajouter_paiement"),
            {
                "eleve_nom": " Awa Diop ",
                "prix": "25000",
                "mode_paiement": "wave",
                "statut": "paye",
            },
        )

        payment = paiement.objects.get()
        self.assertEqual(payment.eleve_nom, "Awa Diop")
        self.assertEqual(payment.prix, Decimal("25000"))
        self.assertRedirects(
            response,
            reverse("paiement:recu", kwargs={"pk": payment.pk}),
        )
        receipt = self.client.get(reverse("paiement:recu", kwargs={"pk": payment.pk}))
        self.assertContains(receipt, "Awa Diop")
        self.assertEqual(receipt.context["paiement"].prix, Decimal("25000"))

    def test_invalid_payment_is_not_saved(self):
        response = self.client.post(
            reverse("paiement:ajouter_paiement"),
            {
                "eleve_nom": "Awa Diop",
                "prix": "-1",
                "mode_paiement": "wave",
                "statut": "paye",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(paiement.objects.count(), 0)
        self.assertTrue(response.context["form"]["prix"].errors)

    def test_receipt_returns_404_for_unknown_payment(self):
        response = self.client.get(
            reverse("paiement:recu", kwargs={"pk": 9999})
        )

        self.assertEqual(response.status_code, 404)

    def test_total_includes_only_confirmed_payments(self):
        paiement.objects.create(
            eleve_nom="Awa Diop",
            prix=Decimal("25000"),
            mode_paiement="wave",
            statut="paye",
        )
        paiement.objects.create(
            eleve_nom="Moussa Fall",
            prix=Decimal("10000"),
            mode_paiement="especes",
            statut="en_attente",
        )

        response = self.client.get(reverse("paiement:list_paiement"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_encaisse"], Decimal("25000"))
