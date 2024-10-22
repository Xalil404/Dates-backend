from django.apps import AppConfig

class ProfileApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profileAPI'

    def ready(self):
        import profileAPI.signals
