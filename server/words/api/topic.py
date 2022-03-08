from rest_framework import serializers

from server.words.api.word import WordSerializer
from server.words.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True)

    class Meta:
        model = Topic
        fields = ("id", "name", "image", "words")
