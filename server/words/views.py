import json

from django.db.models import Prefetch, Q, FilteredRelation, F
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .api.topic import TopicSerializer
from .models import Word, Topic


def words(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        words_qs = Word.objects.annotate(
            user_words=FilteredRelation(
                "userword", condition=Q(userword__user=request.user)
            ),
            status=F("user_words__status")
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
