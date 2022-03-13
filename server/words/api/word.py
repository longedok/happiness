from typing import Any

from celery.worker.request import Request
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from server.words.models import UserWord
from server.words.models import Word


class WordSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    audio = serializers.SerializerMethodField()
    date_display = serializers.DateField(format="%-d %b %Y", source="date")

    class Meta:
        model = Word
        fields = (
            "id", "word", "translation", "transcription", "date", "status", "topic",
            "audio", "date_display",
        )

    def get_audio(self, obj):
        return obj.oxford_data.get("audio_file")


class WordViewSet(GenericViewSet):
    queryset = Word.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(methods=["POST"], detail=True)
    def set_new(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        UserWord.objects.filter(user=request.user, word_id=kwargs["pk"]).delete()
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=True)
    def set_learning(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        self._set_status(UserWord.Status.LEARNING)
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=True)
    def set_learned(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        self._set_status(UserWord.Status.LEARNED)
        return Response(status=status.HTTP_201_CREATED)

    def _set_status(self, learning_status: UserWord.Status) -> None:
        word = get_object_or_404(Word, pk=self.kwargs["pk"])
        UserWord.objects.update_or_create(
            user=self.request.user, word=word, defaults={"status": learning_status}
        )
