from celery import shared_task

from .models import Word
from .logic.oxford import update_oxford_data


@shared_task
def fetch_oxford_data(word_id: str) -> None:
    word = Word.objects.get(pk=word_id)
    update_oxford_data(word)
