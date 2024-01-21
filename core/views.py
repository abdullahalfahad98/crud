from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render (request,"core/home.html", {})

def AddStudent(request):
    if request.method== 'POST' or request.method== 'post':
        print("***********")
        print("Added")
        roll= request.POST.get("roll")
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("address")
        address=request.POST.get("address")
    # else:
    #     print("Not worked")
        
        s=Student()
        s.roll = roll
        s.name = name
        s.email = email
        s.phone = phone
        s.address = address

        s.save()

        
    return render(request,'core/add.html', {})