from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_cour(request):
    return render(request , "cours/list_cour.html")