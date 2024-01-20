from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render (request,"core/home.html", {})

def AddStudent(request):
    if request.method== 'POST' or request.method== 'post':
        print("*********")
    return render(request,'core/add.html', {})