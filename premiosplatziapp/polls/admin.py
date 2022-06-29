from django.contrib import admin
from .models import Choice, Question          # El "." significa que estamos accediendo a la carpeta actual polls.

class ChoiceInline(admin.StackedInline):    # Le agrega la opcion de poner respuestas a la hora de crear preguntas.
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]    # Ordena las respuestas
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_published_recently")    # Hace que se vea los campos que le definimos.
    list_filter = ["pub_date"]    # Filtra el campo pub_date
    search_fields = ["question_text"]    # Es un cuadro de busqueda para encontrar una pregunta a travez de su texto.


admin.site.register(Question, QuestionAdmin)
