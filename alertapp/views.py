from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *
# Create your views here.
class DetectedPersonViewSet(viewsets.ModelViewSet):
    queryset = DetectedPerson.objects.all()
    serializer_class = DetectedPersonSerializer

class SnapShotViewSet(viewsets.ModelViewSet):
    queryset = Snapshot.objects.all()
    serializer_class = SnapshotSerializer