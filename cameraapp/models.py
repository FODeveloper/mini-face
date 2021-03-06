from django.db import models

# Create your models here.

class Position(models.Model):
    position = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.position}'

class Camera(models.Model):
    name = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    stream_url = models.URLField(unique=True)

    def __str__(self):
        return f'{self.name} installed in {self.position}'

