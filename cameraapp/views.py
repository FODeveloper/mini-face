from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *


import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


# Create your views here.
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

    def create(self, request):
        image = request.FILES['image']
        file_path = os.path.join(settings.IMAGES_ROOT, image.name)
        path = default_storage.save(file_path, ContentFile(image.read()))
        return super().create(request)
