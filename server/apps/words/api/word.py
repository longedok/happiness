from rest_framework import serializers

from server.apps.words.models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ("id", "word", "translation", "transcription", "date")
