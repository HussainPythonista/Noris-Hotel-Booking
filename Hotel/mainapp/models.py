from django.db import models

# Create your models here.
class Rooms(models.Model):
    type_room = models.CharField(blank=True, max_length=100)
    room_description= models.CharField(blank=True, max_length=100)
    image = models.ImageField(upload_to="pics")
    Price = models.IntegerField(blank=True, null=True)
