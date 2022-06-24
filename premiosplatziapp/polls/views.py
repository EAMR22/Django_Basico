from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    }) # render lleva 3 parametros: el 1 la respuesta, el 2 la ubicacion del template, el 3 un objeto con las variables usadas por el template.


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) 
    return render(request, "polls/detail.html", {
        "question": question
    }) # El error 404 lleva 2 parametros: EL 1 el modelo y el 2 el valor a ejecutar internamente en la funcion get.


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta numero {question_id}")