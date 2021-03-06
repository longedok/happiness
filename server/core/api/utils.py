from django.apps import apps
from django.conf import settings
from rest_framework import serializers


class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model(*settings.AUTH_USER_MODEL.split("."))  # type: ignore
        fields = ("id", "username", "name")
