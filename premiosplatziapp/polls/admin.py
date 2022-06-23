from django.contrib import admin
from .models import Question          # El "." significa que estamos accediendo a la carpeta actual polls.

admin.site.register(Question)
