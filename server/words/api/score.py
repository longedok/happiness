from rest_framework import serializers

from server.words.models import Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ("id", "user", "date", "score", "description")
