from django.db import models
import datetime
# Create your models here.

class EnrollmentDetails(models.Model):
    id=models.IntegerField(primary_key=True)
    enrollment_no=models.CharField(max_length=12,blank=False)
    enrollment_date=models.DateField()
    name=models.CharField(max_length=256)

