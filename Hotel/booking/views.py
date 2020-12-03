from django.shortcuts import render

# Create your views here.
def booking(request):
    if request.method=='POST':
        check_out=request.POST['check_out']
        print(check_out)
    return render(request,'app/book.html')
