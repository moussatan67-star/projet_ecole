from django.db import models

# Create your models here.
class Absence(models.Model) :
    heur_absence=models.DateTimeField(auto_now=True)
    cours_absenter=models.CharField(max_length=50)


    def __str__(self):
        return self.cours_absenter
