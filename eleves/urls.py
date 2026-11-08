from django.urls import path
from . import views

app_name = "eleves"

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>/", views.eleves_detail, name="detail"),
]