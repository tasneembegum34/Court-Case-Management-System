from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from advocate.models import advocateAccounts
from client.models import clientAccounts
#from .forms import InvoiceForm,LineItemForm
from .models import Invoice,LineItem
from django.http import HttpResponse
# Create your views here.
cli_name=""
def generateInvoice(request):
    user_cli=""
    user_ad=""
    cli_name=request.POST['generate_invoice']
    user_cli=clientAccounts.objects.get(username=cli_name)
    user_ad=advocateAccounts.objects.get(username=request.user)
    return render(request,'editableinvoice.html',context={'user_cli':user_cli,'user_ad':user_ad})


def invoice_data(request):
    if request.is_ajax():
        invoice_table=Invoice()
        if 'meta[]' in request.POST:
            meta=request.POST.get('meta[]')
            print(meta)
            meta=meta.split(',')
            meta.pop()
            invoice_table.invoice_no=meta[0]
            invoice_table.client=meta[6]
            invoice_table.date=meta[1]+","+meta[2]
            invoice_table.due_date=meta[3]+","+meta[4]
            balance1=meta[5]
            balance1=float(balance1[3:len(balance1)-1])
            invoice_table.balance=balance1
            print(meta,balance1)
        #inventory
        if 'balance[]' in request.POST:
            balance=request.POST.get('balance[]')
            balance=balance.split(',')
            balance.pop()
            ta=balance[0]
            ta=float(ta[3:len(ta)-1])
            invoice_table.total_amount=ta
            if(invoice_table.balance<ta):
                invoice_table.status=0
            else:
                invoice_table.status=1
            print(balance,ta)
            invoice_table.save()
        if 'data1[]' in request.POST:
            data1=request.POST.get('data1[]')
            data1=data1.split(',')
            data1.pop()
            lineItem_table=LineItem()
            i=0
            while(i<len(data1)):
                lineItem_table.client=invoice_table
                service=data1[i]
                service=service[1:len(service)-1]
                lineItem_table.service=service
                lineItem_table.description=data1[i+1]
                rate=data1[i+2]
                rate=float(rate[3:len(rate)-1])
                lineItem_table.rate=rate
                lineItem_table.noHours=int(data1[i+3])
                price=data1[i+4]
                price=float(price[3:len(price)-1])
                lineItem_table.price=price
                lineItem_table.save()
                i=i+5
            print(data1)
        
        return HttpResponse('/advocateHome/')
    return HttpResponse('FAIL!!!!!')

