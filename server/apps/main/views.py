import json

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from server.apps.words.api.topic import TopicSerializer
from server.apps.words.models import Topic


def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """

    topics = TopicSerializer(Topic.objects.prefetch_related("words").all(), many=True)

    context = {
        "topics": json.dumps(topics.data),
    }

    return render(request, 'main/index.html', context=context)
