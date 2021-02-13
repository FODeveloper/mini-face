from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *
# Create your views here.
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer