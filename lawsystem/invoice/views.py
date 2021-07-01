from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from advocate.models import advocateAccounts
from client.models import clientAccounts
from .forms import InvoiceForm,LineItemForm
from .models import Invoice,LineItem
from django.http import HttpResponse
# Create your views here.

def generateInvoice(request):
    user_cli=""
    user_ad=""
    if request.method == "POST"  and 'updatebtn' in request.POST:
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
    else:
        cli_name=request.POST['generate_invoice']
        user_cli=clientAccounts.objects.get(username=cli_name)
        user_ad=advocateAccounts.objects.get(username=request.user)
    return render(request,'editableinvoice.html',context={'user_cli':user_cli,'user_ad':user_ad})

def invoice_data(request):
    if request.is_ajax():
        if 'data1[]' in request.POST:
            print("came2")
            data1=request.POST.get('data1[]')
            print(data1)
        if 'meta[]' in request.POST:
            meta=request.POST.get('meta[]')
            print(meta)
        if 'balance[]' in request.POST:
            balance=request.POST.get('balance[]')
            print(balance)
        return HttpResponse('/advocateHome/')
        #return render(request,'MyClientList.html')
    # nothing went well
    return HttpResponse('FAIL!!!!!')

