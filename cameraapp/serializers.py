from rest_framework import serializers

from .models import *


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
       model = Position
       fields = "__all__"


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
       model = Camera
       fields = "__all__"
