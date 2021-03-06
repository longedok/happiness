from typing import Final

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

_STATUS_MAX_LENGTH: Final = 20


class UserWord(models.Model):
    class Status(models.TextChoices):
        LEARNING = "learning", _("Learning")
        LEARNED = "learned", _("Learned")

    word = models.ForeignKey("core.Word", on_delete=models.CASCADE, db_index=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="words",
        db_index=True,
    )

    status = models.CharField(
        _("status"),
        choices=Status.choices,
        default=Status.LEARNING,
        max_length=_STATUS_MAX_LENGTH,
    )

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        verbose_name = _("User Word")
        verbose_name_plural = _("User Words")
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_status_valid",
                check=models.Q(status__in=["learning", "learned"]),
            ),
            models.UniqueConstraint(fields=["word", "user"], name="unique_user_word"),
        ]

    def __str__(self) -> str:
        return f"{self.user}: {self.word}"
