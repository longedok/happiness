from django.urls import path

from server.words.views import words, scores


urlpatterns = [
    path("", words, name="words"),
    path("scores", scores, name="scores"),
]
