from rest_framework import serializers

from .imageprocessor import *
from .models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
       model = Person
       fields = ['first_name', 'last_name', 'photo_path']

    def create(self, data):
        encoding = process(data['photo_path'])
        data['encoding'] = encoding
        super().create(data)
        return data

       