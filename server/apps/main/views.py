from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from server.apps.words.models import Topic
from server.apps.words.models import Word


def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """

    context = {
        "words": Word.objects.all(),
        "topics": Topic.objects.prefetch_related("words").all(),
    }

    return render(request, 'main/index.html', context=context)
