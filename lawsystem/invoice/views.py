from django.shortcuts import render
from advocate.models import advocateAccounts
from client.models import clientAccounts
from .forms import InvoiceForm,LineItemForm
from .models import Invoice,LineItem
from django.http import HttpResponse
# Create your views here.

def generateInvoice(request):
    return render(request,'editableinvoice.html')
    """ if request.method == "POST"  and 'updatebtn' in request.POST:
        invoiceDetails=Invoice()
        invoiceDetails.invoice_no=request.POST['invoice_no']
        invoiceDetails.client=user_cli
        invoiceDetails.date=request.POST['date']
        invoiceDetails.due_date=request.POST['due_date']
        invoiceDetails.balance=7.00
        invoiceDetails.total_amount=request.POST.get('total',False)
        print(request.POST.get('total'))
        invoiceDetails.status=0
        invoiceDetails.save()
    else       pass"""
   #context={'user_cli':user_cli,'user_ad':user_ad})

def invoice_data(request):
    if request.is_ajax():
        print("came2")
        data1=request.POST.get('data1[]')
        print(data1)
       
       
    # nothing went well
    return HttpResponse('FAIL!!!!!')