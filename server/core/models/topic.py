from __future__ import annotations

from typing import TYPE_CHECKING, Final

from django.db import models
from django.db.models import Prefetch
from django.utils.translation import gettext_lazy as _

if TYPE_CHECKING:
    from .word import WordQuerySet


_TOPIC_NAME_MAX_LENGTH: Final = 80
_TOPIC_IMAGE_FOLDER: Final = "topics"


class TopicQuerySet(models.QuerySet["Topic"]):
    def prefetch_words(self, words_queryset: WordQuerySet) -> TopicQuerySet:
        return self.prefetch_related(Prefetch("words", queryset=words_queryset))


class Topic(models.Model):
    name = models.CharField(_("name"), max_length=_TOPIC_NAME_MAX_LENGTH)
    image = models.ImageField(_("image"), upload_to=_TOPIC_IMAGE_FOLDER, null=True, blank=True)

    objects = TopicQuerySet.as_manager()

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")

    def __str__(self) -> str:
        return f"{self.name}"
