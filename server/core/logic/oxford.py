from django.utils import timezone

from server.core.oxford import fetch_word
from server.core.models import Word


def update_oxford_data(word: Word) -> None:
    oxford_data = fetch_word(word.word) or {}
    if transcription := oxford_data.get("phonetic_spelling"):
        word.transcription = transcription
    oxford_data["fetched_at"] = timezone.now().timestamp()
    word.oxford_data = oxford_data
    word.save(update_fields=("oxford_data", "transcription"))
