from celery import shared_task

from .logic.oxford import update_oxford_data
from .models import Word


@shared_task  # type: ignore
def fetch_oxford_data(word_id: str) -> None:
    word = Word.objects.get(pk=word_id)
    update_oxford_data(word)
