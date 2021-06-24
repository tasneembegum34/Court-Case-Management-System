from django.db import models
import datetime
# Create your models here.

class clientAccounts(models.Model):
    id=models.IntegerField(primary_key=True,blank=False)
    first_name=models.CharField(max_length=15,blank=True)
    last_name=models.CharField(max_length=15,blank=True)
    dob=models.DateField(default=datetime.date.today)
    age=models.IntegerField(default=0,blank=True)
    gender=models.CharField(max_length=6,blank=True)
    phno=models.CharField(max_length=15,blank=True)
    email=models.EmailField(blank=True)
    username=models.CharField(max_length=255,blank=True)
    password=models.CharField(max_length=255,blank=True)
    hiredAdUsername=models.CharField(max_length=255,blank=True)
    confirmedAds=models.CharField(max_length=30,blank=True)

class sectionNoDetails(models.Model):
    serial_No=models.IntegerField(default=0,primary_key=True)
    section_No=models.CharField(max_length=10,blank=True)
    section_name=models.CharField(max_length=28,blank=True)
    chapter_No=models.CharField(max_length=30,blank=True)
    description=models.CharField(max_length=255,blank=True)
