from django.db import models

class eleves(models.Model):
    nom=models.CharField(max_length=100)
    prenon=models.CharField(max_length=100)
    age=models.IntegerField()
