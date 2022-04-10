from __future__ import annotations

from typing import Final, TYPE_CHECKING

from django.conf import settings
from django.db.models import FilteredRelation, Q, F, Value
from django.db.models.functions import Coalesce
from django.utils.translation import gettext_lazy as _
from django.db import models

if TYPE_CHECKING:
    from django.contrib.auth.models import User


_WORD_MAX_LENGTH: Final = 80


class WordQuerySet(models.QuerySet):
    def with_status(self, user: User | None = None) -> WordQuerySet:
        new_status = Value("new")
        if user:
            return self.annotate(
                user_words=FilteredRelation("userword", condition=Q(userword__user=user)),
                status=Coalesce(F("user_words__status"), new_status),
            )
        else:
            return self.annotate(status=new_status)


class Word(models.Model):
    word = models.CharField(_("Word"), max_length=_WORD_MAX_LENGTH)
    translation = models.CharField(_("Translation"), max_length=_WORD_MAX_LENGTH)
    date = models.DateField(_("Date"), auto_now=True)
    transcription = models.CharField(_("Transcription"), blank=True, max_length=_WORD_MAX_LENGTH)
    oxford_data = models.JSONField(_("Oxford data"), default=dict, blank=True)

    user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through="core.UserWord")

    topic = models.ForeignKey(
        to="core.Topic",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("topic"),
        related_name="words",
    )

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    objects = WordQuerySet.as_manager()

    class Meta:
        verbose_name = _("Word")
        verbose_name_plural = _("Words")

    def __str__(self) -> str:
        return f"{self.word}"
