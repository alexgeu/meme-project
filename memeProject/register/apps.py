from django.apps import AppConfig

class RegisterConfig(AppConfig):
    name = 'register'

    def ready(self):
        print("at ready")
        import register.signals