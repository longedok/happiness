from __future__ import annotations

import operator
import time
from functools import reduce
from typing import Final

from django.core.management.base import BaseCommand
from django.db.models import Q
from server.core.logic.oxford import update_oxford_data
from server.core.models import Word

_FETCH_DELAY_SECONDS: Final[int] = 1


class Command(BaseCommand):
    help = "Fetches oxford data for words"

    def add_arguments(self, parser):
        parser.add_argument("words", nargs="*")

    def handle(self, *args, **options):
        if words := options["words"]:
            q_filter = reduce(operator.or_, (Q(word__iexact=word) for word in words))
            words = list(Word.objects.filter(q_filter))
        else:
            words = list(Word.objects.filter(oxford_data__fetched_at__isnull=True))

        words_number = len(words)
        for word in words:
            update_oxford_data(word)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Fetched data for word {word.word}: {word.oxford_data}"
                )
            )

            if words_number > 1:
                time.sleep(_FETCH_DELAY_SECONDS)
