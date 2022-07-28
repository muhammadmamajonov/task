from tkinter import CASCADE
from django.db import models

# Create your models here.

class Apparat(models.Model):
    apparat_id = models.CharField(max_length=15)

    def __str__(self):
        return self.apparat_id

class Phone(models.Model):
    apparat = models.ForeignKey(Apparat, on_delete = models.CASCADE)
    device_count = models.IntegerField()
    counted_at = models.DateTimeField()

class Data(models.Model):
    apparat_id = models.CharField(max_length=15)
    packet_time = models.IntegerField()
