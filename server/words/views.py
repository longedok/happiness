import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .api.topic import TopicSerializer
from .api.word import WordSerializer
from .models import Word, Topic


def words(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        words_qs = Word.objects.with_status(request.user)
    else:
        words_qs = Word.objects.with_status()

    words_qs = words_qs.order_by("-id")

    topic_serializer = TopicSerializer(Topic.objects.order_by("id"), many=True)
    words_serializer = WordSerializer(words_qs, many=True)

    context = {
        "topics": json.dumps(topic_serializer.data),
        "words": json.dumps(words_serializer.data),
    }

    return render(request, 'main/index.html', context=context)
