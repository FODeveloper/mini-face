from django.db import models
from personapp.models import Person
from cameraapp.models import Camera
# Create your models here.



class Snapshot(models.Model):
    path = models.CharField(max_length=255, unique=True)
    snaphot_time = models.DateTimeField(auto_now=True)
    camera = models.ForeignKey(Camera, on_delete=models.PROTECT)

    def __str__(self):
        return f'Snapshot at {self.snaphot_time} on camera: {self.camera}'



class DetectedPerson(models.Model):
    bb_tlx = models.IntegerField()
    bb_tly = models.IntegerField()
    bb_brx = models.IntegerField()
    bb_bry = models.IntegerField()
    new_encoding = models.CharField(max_length=65536)

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Snapshot = models.ForeignKey(Snapshot, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.person}'
    
    