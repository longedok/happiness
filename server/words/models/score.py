from __future__ import annotations

from typing import Final

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


_TYPE_MAX_LENGTH: Final[int] = 30
_DESCRIPTION_MAX_LENGTH: Final[int] = 255


class Score(models.Model):
    scoreboard = models.ForeignKey(
        "words.Scoreboard",
        on_delete=models.CASCADE,
        related_name="scores",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="scores",
    )

    date = models.DateTimeField(_("Date"), auto_now_add=True)
    score = models.IntegerField(_("score"))
    description = models.CharField(
        _("Description"),
        blank=True,
        max_length=_DESCRIPTION_MAX_LENGTH,
    )

    def __str__(self) -> str:
        return f"Score for {self.scoreboard}"
