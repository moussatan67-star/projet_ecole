from django.db import models

# Create your models here.
class cour(models.Model):
    DEROULEMENT=(("a l'instant","a l'instant"),
                  ("apres midi","apres midi"),
                   ( "soire"   ,"soire"  ),)
    nom=models.CharField(max_length=100)
    heur_deroulement=models.CharField(max_length=100, choices=DEROULEMENT)


    def __str__(self):
        return self.nom