import datetime
from mainapp.models import Room #For access room class in models
from django.db import models
from django.conf import settings # For access the data which stored in auth_user


# Create your models here.
class Booking(models.Model):
    """Django data model Booking"""
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    Check_in = models.DateTimeField(blank=True, default=datetime.datetime.now)
    Check_out = models.DateTimeField(blank=True, default=datetime.datetime.now)
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f'{self.user} booked {self.room} from {self.Check_in} to {self.Check_out}'
