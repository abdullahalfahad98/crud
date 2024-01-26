from django.urls import path
from .views import *
urlpatterns = [
    
    path("",home),
    path("home/",home),
    path("add/",AddStudent),
    # path("delete/",delete_std),
    path("delete/<int:roll>",delete_std),
    path("update/<int:pk>",update_std),
    path("do-update/<int:pk>",do_update_std),
    
]


#git remote add origin https://github.com/abdullahalfahad98/crud.git

#Project Link
#https://www.youtube.com/watch?v=VETRxH88OUM&t=1991s