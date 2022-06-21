from tkinter import CASCADE
from django.db import models

class Question(models.Model):    # En django no es necesario generar un "id" porque automaticamente tiene un incrementador por dentro.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   # En on_delete cuando volvemos a la pregunta, borramos en cascada el resto de las preguntas.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)