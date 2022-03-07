import operator
from functools import reduce

from django.core.management.base import BaseCommand
from django.db.models import Q

from server.apps.words.logic.oxford import update_oxford_data
from server.apps.words.models import Word


class Command(BaseCommand):
    help = "Fetches oxford data for words"

    def add_arguments(self, parser):
        parser.add_argument("words", nargs="*")

    def handle(self, *args, **options):
        if words := options["words"]:
            q_filter = reduce(operator.or_, (Q(word__iexact=word) for word in words))
            words = Word.objects.filter(q_filter)
        else:
            words = Word.objects.filter(oxford_data__fetched_at__isnull=True)

        for word in words:
            update_oxford_data(word)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Fetched data for word {word.word}: {word.oxford_data}"
                )
            )
