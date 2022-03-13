from django.conf import settings
from django.apps import apps
from rest_framework import serializers

from server.words.api.score import ScoreSerializer
from server.words.models import Scoreboard


class ScoreboardUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
        fields = ("id", "username", "first_name")


class ScoreboardSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)
    user_1 = ScoreboardUserSerializer()
    user_2 = ScoreboardUserSerializer()
    user_1_score = serializers.IntegerField()
    user_2_score = serializers.IntegerField()

    class Meta:
        model = Scoreboard
        fields = (
            "id", "name", "user_1", "user_2", "scores", "user_1_score", "user_2_score"
        )
