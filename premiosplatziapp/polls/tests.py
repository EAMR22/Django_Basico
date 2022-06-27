import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question   # El .models es lo mismo que premiosplatziapp.polls.models

#Por lo general se hacen tests de models o vistas en django.
class QuestionModelTests(TestCase):   #Cada test es un metodo de la clase, en este caso Question.

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es el mejor COurse Director de Platzi", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False) # Verifica si el metodo es falso.


def create_question(question_text, days):
    """
    Create a question with the given "question_text", and published the given
    number of days offset to now (negative for questions published in the past,
    positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """In no question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index")) # Hace una request http a la url del index, se trae la respuesta y la guarda en response.
        self.assertEqual(response.status_code, 200)   # Verifica que la peticion traida sea igual a 200.
        self.assertContains(response, "No polls are available")    
        self.assertQuerysetEqual(response.context["latest_question_list"], []) 

    def text_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on the index page.
        """
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")     # Enviamos un mensaje a una url mal escrita.
        self.assertQuerysetEqual(response.context["latest_question_list"], [])      #Evalua que la variable no contiene nada.

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the index page.
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question]) 
