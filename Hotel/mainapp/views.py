from django.shortcuts import render
from .models import Room, Room_Type
# Create your views here.
def home(request):
    roomCate=dict(sorted(Room_Type.ROOM_CATEGORIES,reverse=True)).values()
    roomUrl=Room_Type.objects.all()
    zipped=list(zip(roomCate,roomUrl))
    room_list=[]
    for i in zipped:
        room_list.append(i)
    context={'rooms_list':room_list}
    return render(request,'index.html',context)
