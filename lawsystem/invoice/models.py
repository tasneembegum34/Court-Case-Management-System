from django.db import models
import datetime
# Create your models here.
class Invoice(models.Model):
    invoice_no=models.CharField(max_length=30,blank=True)
    client = models.CharField(max_length=100,blank=True)
    date = models.DateField(default=datetime.date.today)
    due_date = models.DateField(default=datetime.date.today)
    balance=models.DecimalField(max_digits=9, decimal_places=2,default=0.0)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.client)
    
    def get_status(self):
        return self.status

    # def save(self, *args, **kwargs):
        # if not self.id:             
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

class LineItem(models.Model):
    client = models.ForeignKey(Invoice, on_delete=models.CASCADE,default=1)
    service = models.TextField(blank=True,max_length=255)
    description = models.TextField(blank=True,max_length=254)
    rate = models.DecimalField(max_digits=9, decimal_places=2,blank=True)
    noHours = models.IntegerField(default=1,blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2,default=0.0)

    def __str__(self):
        return str(self.client)
