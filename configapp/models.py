from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Config(models.Model):
    tolerance = models.FloatField(default=0.6)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.user.username}\'s configurations'