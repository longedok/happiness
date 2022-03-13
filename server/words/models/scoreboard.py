from __future__ import annotations

from typing import Final

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

_NAME_MAX_LENGTH: Final[int] = 100
_DESCRIPTION_MAX_LENGTH: Final[int] = 255


class Scoreboard(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=_NAME_MAX_LENGTH,
    )

    user_1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="+",
    )

    user_2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="+",
    )

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    description = models.CharField(
        _("Description"),
        blank=True,
        max_length=_DESCRIPTION_MAX_LENGTH,
    )

    def __str__(self) -> str:
        return f"{self.name}"
