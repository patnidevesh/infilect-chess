from django.urls import path
from . import views

urlpatterns = [
    path("chess/<slug>", views.index, name="index"),
]