
import datetime
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from mainapp.models import Room_Type,Room
from django.shortcuts import render
from .bookingFunction import avalablity
from .models import Booking
from django.utils.timezone import make_aware

# Create your views here.

#The Objectives of Room
#1) . Make a booking form for a user
#2).The User provides only dates and categories
#3).The User remain unaware of room no.A room from the category is randomly booked
#4).Use the Avaliblity function to check the room avaliblity
def booking(request,room):
    if request.method=='POST':
    #This is from booking page
        get_roomType=Room_Type.objects.get(roomtype=request.POST['type'])
        roomid=get_roomType.id
        getout=request.POST['check_out']  
        check_out=datetime.datetime.strptime(getout,'%m/%d/%Y %H:%M %p').strftime('%Y-%m-%d %H:%M:%S')
        getin=request.POST['check_in']  
        check_in=datetime.datetime.strptime(getin,'%m/%d/%Y %H:%M %p').strftime('%Y-%m-%d %H:%M:%S')
        check_in=make_aware(datetime.datetime.strptime(check_in,'%Y-%m-%d %H:%M:%S'))
        check_out=make_aware(datetime.datetime.strptime(check_out,'%Y-%m-%d %H:%M:%S'))
    
    #This can set the values id to roomtype id
        room_list=Room.objects.filter(room_type=roomid)
        avalible_rooms=[]
        for room in room_list:
            if avalablity.check_avaliblity(room,check_in,check_out):
                avalible_rooms.append(room)
        for room_book in avalible_rooms:
                    roomForBook=room_book
                    if len(avalible_rooms)>0:
                        book_room=Booking.objects.create(
                            user=request.user,
                            room=roomForBook,
                            Check_in=check_in,
                            Check_out=check_out
                        )
                        book_room.save()
                        return HttpResponse(book_room)
        else:
                    return HttpResponse("The room is not avalible")
    rooms=Room_Type.objects.all()#For get all Room_Type
    roomCate=dict(sorted(Room_Type.ROOM_CATEGORIES,reverse=True)).values()
    zipped=zip(roomCate,rooms)
    room_in_list=Room_Type.objects.get(roomtype=room)#Get clicked values
    str_roomlist=str(room_in_list)#It only get values in string format only so we change values in str formate
    values_roomList=dict(Room_Type.ROOM_CATEGORIES).get(str_roomlist)
    list_element=[]
    for _ in range(1):
        list_element.append((str_roomlist,values_roomList))
    print(list_element)
    context={
    'types':zipped,
    'room_in_list':list_element
    }

    return render(request,'app/book.html',context)