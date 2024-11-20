from django.apps import AppConfig


class AppProjectConfig(AppConfig):
<<<<<<< HEAD
    name = 'app_project'
=======
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_project'

    def ready(self):
        import app_project.signals
>>>>>>> Parte 3
