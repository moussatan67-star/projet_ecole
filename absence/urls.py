from django.urls import path
from . import views

app_name = "absence"
urlpatterns = [
    path("", views.list_absence, name="list_absence"),
]
