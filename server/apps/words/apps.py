from django.apps import AppConfig


class WordsConfig(AppConfig):
    name = "server.apps.words"

    def ready(self) -> None:
        from . import receivers
