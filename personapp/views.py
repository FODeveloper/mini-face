from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *
# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

