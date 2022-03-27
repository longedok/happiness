from rest_framework import serializers

from server.core.api.utils import NestedUserSerializer
from server.core.models import Score


class ScoreSerializer(serializers.ModelSerializer):
    user = NestedUserSerializer()
    date_display = serializers.DateTimeField(format="%-d %b %Y", source="date")

    class Meta:
        model = Score
        fields = ("id", "user", "date", "date_display", "score", "description")
