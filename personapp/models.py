from django.db import models
import json
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # features vector with 128 values
    encoding = models.CharField(max_length=65536)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'