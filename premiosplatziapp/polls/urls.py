from django.urls import path

from . import views          # El . es la carpeta polls.

urlpatterns = [
    path("", views.index, name="index")
]