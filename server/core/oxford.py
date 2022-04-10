from __future__ import annotations

import logging
from typing import Any, Iterable, TypeVar

import requests
from django.conf import settings
from requests import RequestException

BASE_URL = "https://od-api.oxforddictionaries.com/api/v2"
ENTRIES_URL = f"{BASE_URL}/entries/en-gb"
OXFORD_API_TIMEOUT = 10

HEADERS = {
    "app_id": settings.OXFORD_API_APP_ID,
    "app_key": settings.OXFORD_API_APP_KEY,
}


logger = logging.getLogger(__name__)


class OxfordAPIError(Exception):
    def __init__(self, message: str, status_code: int | None = None) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(message)


def _get_entry(word_id: str) -> dict[str, Any]:
    try:
        response = requests.get(
            f"{ENTRIES_URL}/{word_id}", headers=HEADERS, timeout=OXFORD_API_TIMEOUT
        )
    except RequestException as exc:
        raise OxfordAPIError(str(exc))

    if 200 <= response.status_code < 300:
        return response.json()
    else:
        raise OxfordAPIError(response.text, response.status_code)


T = TypeVar("T")


def _first(items: Iterable[T]) -> T | None:
    return next(iter(items), None)


def fetch_word(word_id: str) -> dict[str, Any] | None:
    try:
        data = _get_entry(word_id.lower())
    except OxfordAPIError as exc:
        logger.exception(exc)
        return None

    if not (result := _first(data.get("results", []))):
        return None

    if not (lexical_entry := _first(result.get("lexicalEntries", []))):
        return None

    if not (entry := _first(lexical_entry.get("entries", []))):
        return None

    if not (pronunciation := _first(entry.get("pronunciations", []))):
        return None

    return {
        "audio_file": pronunciation.get("audioFile"),
        "dialects": pronunciation.get("dialects"),
        "phonetic_notation": pronunciation.get("phoneticNotation"),
        "phonetic_spelling": pronunciation.get("phoneticSpelling"),
    }
