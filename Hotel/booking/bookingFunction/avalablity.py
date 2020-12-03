#This Python file used to chech the avaliblity
import datetime
from booking.models import Booking
from mainapp.models import Room
def check_avaliblity(room,Check_in,Check_out):
    avaliblity_list=[]  #It will return binch of True and False
    booking_list=Booking.objects.filter(room=room)#It will check bookings of specific room ex:101
    for booking in booking_list:
        if booking.Check_in>Check_out or booking.Check_out<Check_in: 
            #booking.check_in and booking.check_out is existing booking
            avaliblity_list.append(True)
        else:
            avaliblity_list.append(False) #If any of list in avaliblity_list is get False The Booking cannot happend
    return all(avaliblity_list)
    #all() only return all of item in list True
