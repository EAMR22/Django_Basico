from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.all()
#     return render(request, "polls/index.html", {
#         "latest_question_list": latest_question_list
#     }) # render lleva 3 parametros: el 1 la respuesta, el 2 la ubicacion del template, el 3 un objeto con las variables usadas por el template.


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id) 
#     return render(request, "polls/detail.html", {
#         "question": question
#     }) # El error 404 lleva 2 parametros: EL 1 el modelo y el 2 el valor a ejecutar internamente en la funcion get.


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {
#         "question": question
#     })


# Es una generic view
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions """ # El "[:5]" nos dice que solo traera los primeros 5 elementos del arreglo.
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5] # El "-" significa que traera los datos de los mas recientes a las mas antiguas.

class DetailView(generic.DetailView):   # El __lte nos indica que es menor o igual.
    model = Question
    template_name = "polls/detail.html"

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# Es una function based views
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