from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {
        "question": question
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) # choice hace referencia al name del formulario de detail.html
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No elegistes una respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,))) # Redirige al usuario hacia una nueva pagina.
        # (question.id,) Es una tupla de un elemento.