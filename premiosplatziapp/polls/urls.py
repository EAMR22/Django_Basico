from django.urls import path

from . import views          # El . es la carpeta polls.

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"), # Con .as_view lo que hace es renderizar el template que corresponde a la vista.
    # ex: /polls/3/ aqui accedemos al detalle de la pregunta numero 3.
    path("<int:pk>/detail/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/3/results
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"), # COn pk accedemos a la llave primaria de Question.
    # ex: /polls/3/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]