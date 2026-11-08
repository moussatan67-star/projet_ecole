from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_absence(requeste):
    return render(requeste , "absence/list_absence.html")
