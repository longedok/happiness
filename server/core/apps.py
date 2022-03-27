from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    name = "server.core"
    verbose_name = _("Happiness")
    label = "core"

    def ready(self) -> None:
        from . import receivers
