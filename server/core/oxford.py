from __future__ import annotations

import logging
from typing import Any, Iterable

from django.conf import settings

import requests
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


def _get_entry(word_id: str) -> dict[str, Any] | None:
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


def _first(items: Iterable) -> Any:
    return next(iter(items), None)


def fetch_word(word_id: str) -> dict[str, Any] | None:
    try:
        data = _get_entry(word_id.lower())
    except OxfordAPIError as exc:
        logger.exception(exc)
        return

    if not (result := _first(data.get("results", []))):
        return

    if not (lexical_entry := _first(result.get("lexicalEntries", []))):
        return

    if not (entry := _first(lexical_entry.get("entries", []))):
        return

    if not (pronunciation := _first(entry.get("pronunciations", []))):
        return

    return {
        "audio_file": pronunciation.get("audioFile"),
        "dialects": pronunciation.get("dialects"),
        "phonetic_notation": pronunciation.get("phoneticNotation"),
        "phonetic_spelling": pronunciation.get("phoneticSpelling")
    }
