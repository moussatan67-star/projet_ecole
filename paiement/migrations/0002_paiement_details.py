from django.db import migrations, models
import django.core.validators


def normalize_payment_methods(apps, schema_editor):
    Payment = apps.get_model("paiement", "paiement")
    Payment.objects.filter(mode_paiement="liquide").update(mode_paiement="especes")
    Payment.objects.filter(mode_paiement="par carte").update(mode_paiement="carte")


def restore_payment_methods(apps, schema_editor):
    Payment = apps.get_model("paiement", "paiement")
    Payment.objects.filter(mode_paiement="especes").update(mode_paiement="liquide")
    Payment.objects.filter(mode_paiement="carte").update(mode_paiement="par carte")


class Migration(migrations.Migration):

    dependencies = [
        ("paiement", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="paiement",
            options={
                "ordering": ["-heure", "-id"],
                "verbose_name": "paiement",
                "verbose_name_plural": "paiements",
            },
        ),
        migrations.AddField(
            model_name="paiement",
            name="eleve_nom",
            field=models.CharField(default="Etudiant", max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="paiement",
            name="prix",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=12,
                validators=[django.core.validators.MinValueValidator(0.01)],
            ),
        ),
        migrations.AlterField(
            model_name="paiement",
            name="mode_paiement",
            field=models.CharField(
                choices=[
                    ("especes", "Especes"),
                    ("carte", "Carte bancaire"),
                    ("wave", "Wave / mobile money"),
                    ("virement", "Virement bancaire"),
                ],
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="paiement",
            name="statut",
            field=models.CharField(
                choices=[("paye", "Paye"), ("en_attente", "En attente")],
                default="paye",
                max_length=20,
            ),
        ),
        migrations.RunPython(normalize_payment_methods, restore_payment_methods),
    ]
