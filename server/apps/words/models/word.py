from typing import Final

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models

_WORD_MAX_LENGTH: Final = 80
_STATUS_MAX_LENGTH: Final = 20


class Word(models.Model):
    word = models.CharField(_("word"), max_length=_WORD_MAX_LENGTH)
    translation = models.CharField(_("translation"), max_length=_WORD_MAX_LENGTH)
    date = models.DateField(_("date"), auto_now=True)

    user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through="words.UserWord")

    topic = models.ForeignKey(
        to="words.Topic", on_delete=models.SET_NULL, null=True, verbose_name=_("topic"), related_name="words"
    )

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Word")
        verbose_name_plural = _("Words")

    def __str__(self) -> str:
        return f"{self.word}"
