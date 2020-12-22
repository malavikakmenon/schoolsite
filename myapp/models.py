from django.db import models

# Create your models here.
class addstudent(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    studentid= models.CharField(max_length=10)
    std=models.CharField(max_length=2)
    email= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    phoneno= models.CharField(max_length=10)
    address= models.CharField(max_length=250)

	# check_me_out = models.BooleanField(required=False)