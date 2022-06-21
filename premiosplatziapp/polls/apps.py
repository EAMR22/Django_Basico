from django.apps import AppConfig


class PollsConfig(AppConfig):     # Hace que nuestra aplicacion funcione dentro del proyecto.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
