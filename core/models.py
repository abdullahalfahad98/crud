from django.db import models
from django.core.validators import RegexValidator, ValidationError

# Create your models here.
class Student(models.Model):
    roll= models.IntegerField()
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    address=models.TextField()
    


    def clean_phone(self):
        if not self.phone:
            raise ValidationError("Phone number cannot be empty.")
        elif len(self.phone) != 11:
            raise ValidationError("Phone number must be 11 digits (01*********)")
        elif not self.phone.startswith("01"):
            raise ValidationError("Phone number must start with '01'.")
        elif not self.phone[2:].isdigit():
            raise ValidationError("Phone number must contain only digits after '01'.")