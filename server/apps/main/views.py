import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.db.models import Prefetch, F, Max, Q

from server.apps.words.models import Word
from server.apps.words.api.topic import TopicSerializer
from server.apps.words.models import Topic


def index(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        words_qs = Word.objects.annotate(
            status=Max("userword__status", filter=Q(userword__user=request.user))
        )
    else:
        words_qs = Word.objects.annotate(status=None).all()

    prefetch = Prefetch("words", queryset=words_qs)

    topic_serializer = TopicSerializer(
        Topic.objects.prefetch_related(prefetch).all(), many=True
    )

    context = {
        "topics": json.dumps(topic_serializer.data),
    }

    return render(request, 'main/index.html', context=context)
