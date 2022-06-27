import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question   # El .models es lo mismo que premiosplatziapp.polls.models

#Por lo general se hacen tests de models o vistas en django.
class QuestionModelTests(TestCase):   #Cada test es un metodo de la clase, en este caso Question.

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es el mejor COurse Director de Platzi", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False) # Verifica si el metodo es falso.
