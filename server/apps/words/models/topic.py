from typing import Final

from django.utils.translation import gettext_lazy as _
from django.db import models

_TOPIC_NAME_MAX_LENGTH: Final = 80
_TOPIC_IMAGE_FOLDER: Final = "topics"


class Topic(models.Model):
    name = models.CharField(_("name"), max_length=_TOPIC_NAME_MAX_LENGTH)
    image = models.ImageField(_("image"), upload_to=_TOPIC_IMAGE_FOLDER, null=True, blank=True)

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")

    def __str__(self) -> str:
        return f"{self.name}"
