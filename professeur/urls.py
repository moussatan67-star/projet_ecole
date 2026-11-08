from django.urls import path
from . import views

app_name = "professeur"
urlpatterns = [
    path("", views.list_professeur, name="list_professeur"),
]