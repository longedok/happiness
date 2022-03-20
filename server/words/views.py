import json
import logging

from django.db.models import Sum, F, Q, Prefetch
from django.db.models.functions import Coalesce
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views

from .api.scoreboard import ScoreboardSerializer
from .api.topic import TopicSerializer
from .api.word import WordSerializer
from .models import Word, Topic, Scoreboard, Score
from .forms import UserCreationForm, AuthenticationForm

logger = logging.getLogger(__name__)


def words(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        words_qs = Word.objects.with_status(request.user)
    else:
        words_qs = Word.objects.with_status()

    words_qs = words_qs.order_by("-date")

    topic_serializer = TopicSerializer(Topic.objects.order_by("id"), many=True)
    words_serializer = WordSerializer(words_qs, many=True)

    context = {
        "topics": json.dumps(topic_serializer.data),
        "words": json.dumps(words_serializer.data),
        "page": "words",
    }

    return render(request, 'words/words.html', context=context)


def scores(request: HttpRequest) -> HttpResponse:
    user_id = request.user.id if request.user.is_authenticated else None
    scoreboards = (
        Scoreboard.objects
        .prefetch_related(
            Prefetch("scores", queryset=Score.objects.select_related("user"))
        )
        .select_related("user_1", "user_2")
        .annotate(
            user_1_score=Coalesce(
                Sum("scores__score", filter=Q(scores__user=F("user_1"))), 0
            )
        )
        .annotate(
            user_2_score=Coalesce(
                Sum("scores__score", filter=Q(scores__user=F("user_2"))), 0
            )
        )
        .filter(
            Q(user_1=user_id) | Q(user_2=user_id)
        )
        .only(
            "id",
            "name",
            "user_title",
            "user_1__first_name",
            "user_1__username",
            "user_2__first_name",
            "user_2__username",
        )
    )

    scoreboard_serializer = ScoreboardSerializer(scoreboards, many=True)

    context = {
        "scoreboards": json.dumps(scoreboard_serializer.data),
        "page": "scores",
    }

    return render(request, 'words/scores.html', context=context)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("signup-success")
    template_name = "words/signup.html"


class SignUpSuccessView(generic.TemplateView):
    template_name = "words/signup_success.html"


class LogInView(auth_views.LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("words")
    template_name = "words/login.html"
