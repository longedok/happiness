from django.apps import AppConfig


class WordsConfig(AppConfig):
    name = "server.words"

    def ready(self) -> None:
        from . import receivers
