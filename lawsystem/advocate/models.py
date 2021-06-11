from django.db import models
import datetime
# Create your models here.
class advocateAccounts(models.Model):
    id=models.IntegerField(primary_key=True,blank=False)
    first_name=models.CharField(max_length=15,blank=True)
    last_name=models.CharField(max_length=15,blank=True)
    email=models.EmailField(blank=True)
    username=models.CharField(max_length=255,blank=True)
    password=models.CharField(max_length=255,blank=True)
    phno=models.CharField(max_length=15,blank=True)
    dob=models.DateField(default=datetime.date.today)
    age=models.IntegerField(default=0,blank=True)
    gender=models.CharField(max_length=6,blank=True)
    experience=models.IntegerField(default=0,blank=True)
    expertise=models.CharField(max_length=15,blank=True)
    qualification=models.CharField(max_length=255,blank=True)
    address=models.CharField(max_length=255,blank=True)
    description=models.TextField(max_length=300,blank=True)
   
