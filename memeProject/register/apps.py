from django.apps import AppConfig

class RegisterConfig(AppConfig):
    """
    RegisterConfig calls the signals when a new user is created. For each new registered user, a profile will be created
    """
    name = 'register'

    def ready(self):
        import register.signals