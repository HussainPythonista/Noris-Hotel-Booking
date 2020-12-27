from django.db import models
class Room_Type(models.Model):
    """Django data model Room_Type"""
    ROOM_CATEGORIES={
    ('Elt','Elite'),
    ('Lux','Luxury'),
    ('Sig','Signature')
    }

    image = models.ImageField(upload_to="pics")
    roomtype = models.CharField(choices=ROOM_CATEGORIES,max_length=20)
    price = models.CharField(blank=True, max_length=100)
    def __str__(self):
        return f'{self.roomtype}'

class Room(models.Model):
    #price=models.ForeignKey(Room_Type,     on_delete=models.CASCADE,default='')
    room_no = models.IntegerField(blank=True, null=True)
    room_type=models.ForeignKey(Room_Type, on_delete=models.CASCADE)
    beds = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Room No {self.room_no} in {self.room_type} Categoriy with {self.beds} beds for {self.capacity} people'
