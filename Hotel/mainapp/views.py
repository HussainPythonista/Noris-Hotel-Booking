from django.shortcuts import render
from .models import Room_Type
# Create your views here.
def home(request):
    rooms=Room_Type.objects.all()
    context={'rooms':rooms}
    return render(request,'index.html',context)
