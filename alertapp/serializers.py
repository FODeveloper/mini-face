from rest_framework import serializers
from .models import *


class SnapshotSerializer(serializers.ModelSerializer):
    class Meta:
       model = Snapshot
       fields = "__all__"

class DetectedPersonSerializer(serializers.ModelSerializer):
    class Meta:
       model = DetectedPerson
       fields = "__all__"