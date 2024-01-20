from django.urls import path
from .views import *
urlpatterns = [
    
    path("",home),
    path("home/",home),
    path("add/",AddStudent),
]


#git remote add origin https://github.com/abdullahalfahad98/crud.git