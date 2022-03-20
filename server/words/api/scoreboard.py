from rest_framework import serializers

from server.words.api.score import ScoreSerializer
from server.words.api.utils import NestedUserSerializer
from server.words.models import Scoreboard


class ScoreboardSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)
    user_1 = NestedUserSerializer()
    user_2 = NestedUserSerializer()
    user_1_score = serializers.IntegerField()
    user_2_score = serializers.IntegerField()

    class Meta:
        model = Scoreboard
        fields = (
            "id", "name", "user_title", "user_1", "user_2", "scores", "user_1_score",
            "user_2_score",
        )
