from django.urls import path
from . import views

app_name = "cour"
urlpatterns = [
    path("", views.list_cour, name="list_cour"),
]