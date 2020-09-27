from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Cube(models.Model):
    solver = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    cuber = models.CharField(max_length=64)
    best_time = models.TimeField()
    worst_time = models.TimeField()

    def __str__(self):
        return self.cuber