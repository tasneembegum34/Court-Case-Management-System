from django.db import models
import datetime
# Create your models here.
class Invoice(models.Model):
    invoice_no=models.CharField(max_length=30,blank=True)
    client = models.CharField(max_length=100,blank=True)
    date = models.CharField(max_length=20,blank=True)
    due_date = models.CharField(max_length=20,blank=True)
    balance=models.DecimalField(max_digits=9, decimal_places=2,default=0.0)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
        # if not self.id:             
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

class LineItem(models.Model):
    invoice_no = models.CharField(max_length=30,blank=True)
    service = models.TextField(blank=True,max_length=255)
    description = models.TextField(blank=True,max_length=254)
    rate = models.DecimalField(max_digits=9, decimal_places=2,blank=True)
    noHours = models.IntegerField(default=1,blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2,default=0.0)


