from django.apps import AppConfig


class AppConfig(AppConfig):
    name = "app"

    def ready():
        import app.signals  # noqa
