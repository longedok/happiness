from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from server.apps.words.models import Word, Topic, UserWord


@admin.register(Word)
class WordAdmin(admin.ModelAdmin[Word]):
    """Admin panel for `Word` model."""

    list_display = ("word", "translation", "transcription", "topic", "date")
    list_filter = ("topic", "date")
    fields = ("word", "translation", "topic", "transcription")

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).select_related("topic")


@admin.register(Topic)
class WordAdmin(admin.ModelAdmin[Topic]):
    """Admin panel for `Topic` model."""


@admin.register(UserWord)
class UserWordAdmin(admin.ModelAdmin[UserWord]):
    """Admin panel for `UserWord` model."""

    list_display = ("word", "user", "status")
