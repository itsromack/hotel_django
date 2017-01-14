from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Unit(models.Model):
    id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField(default=1)
    bed_rooms = models.IntegerField(default=1)
    max_persons = models.IntegerField(default=1)
    aircon = models.IntegerField(default=1)
    description = models.CharField(max_length=255)

class Client(models.Model):
    id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    email = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    birthdate = models.DateTimeField()