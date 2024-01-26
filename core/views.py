from django.shortcuts import render,redirect
from .models import Student

# Create your views here.

#Create Student data
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
        return redirect("/core/home")

        
    return render(request,'core/add.html', {})


#read Student data
def home(request):
    std = Student.objects.all()
    return render (request,"core/home.html", {'std':std })



def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect("/core/home")


def update_std(request,pk):
    up=Student.objects.get(pk=pk)

    return render(request,'core/update.html',{'up':up})

def do_update_std(request,pk):
    up_roll= request.POST.get("roll")
    up_name=request.POST.get("name")
    up_email=request.POST.get("email")
    up_phone=request.POST.get("address")
    up_address=request.POST.get("address")

    up=Student.objects.get(pk=pk)
    
    up.roll = up_roll
    up.name = up_name
    up.email = up_email
    up.phone = up_phone
    up.address = up_address

    up.save()
    return redirect("/core/home")




