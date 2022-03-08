from django.urls import path

from server.words.views import words


urlpatterns = [
    path("", words, name="words"),
]
