from django.db import models

# Create your models here.
class professeur(models.Model):
    prenon=models.CharField(max_length=100)
    nom=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.nom
