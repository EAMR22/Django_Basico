import datetime

from tkinter import CASCADE
from django.db import models
from django.utils import timezone

class Question(models.Model):    # En django no es necesario generar un "id" porque automaticamente tiene un incrementador por dentro.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   # En on_delete cuando volvemos a la pregunta, borramos en cascada el resto de las preguntas.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text