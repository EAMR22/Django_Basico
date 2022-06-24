from django.urls import path

from . import views          # El . es la carpeta polls.

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/3/ aqui accedemos al detalle de la pregunta numero 3.
    path("<int:question_id>/detail/", views.detail, name="detail"),
    # ex: /polls/3/results
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/3/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]