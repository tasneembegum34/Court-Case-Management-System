from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from advocate.models import advocateAccounts
from client.models import clientAccounts
from .models import Invoice,LineItem
from django.http import HttpResponse
from .utils import render_to_pdf
from django.template.loader import get_template
import pdfkit

# Create your views here.
cli_name=""
def generateInvoice(request):
    user_cli=""
    user_ad=""
    cli_name=request.POST['generate_invoice']
    user_cli=clientAccounts.objects.get(username=cli_name)
    user_ad=advocateAccounts.objects.get(username=request.user)
    return render(request,'editableinvoice.html',context={'user_cli':user_cli,'user_ad':user_ad})

def viewInvoice(request):
    invoice_table=""
    if request.method=='POST':
        cli_name=request.POST['viewInvoice']
        invoice_table=Invoice.objects.filter(client=cli_name)
    return render(request,'invoiceDetails.html',{'invoice_table':invoice_table})

def invoice_data(request):
    if request.is_ajax():
        invoice_table=Invoice()
        if 'meta[]' in request.POST:
            meta=request.POST.get('meta[]')
            meta=meta.split(',')
            meta.pop()
            invoice_table.invoice_no=meta[0]
            invoice_table.client=meta[6]
            invoice_table.date=meta[1]+","+meta[2]
            invoice_table.due_date=meta[3]+","+meta[4]
            balance1=meta[5]
            balance1=float(balance1[3:len(balance1)-1])
            invoice_table.balance=balance1
        #inventory
        if 'balance[]' in request.POST:
            balance=request.POST.get('balance[]')
            balance=balance.split(',')
            balance.pop()
            ta=balance[0]
            ta=float(ta[3:len(ta)-1])
            invoice_table.total_amount=ta
            if(invoice_table.balance==0):
                invoice_table.status=1
            else:
                invoice_table.status=0
            invoice_table.save()
        if 'data1[]' in request.POST:
            data1=request.POST.get('data1[]')
            data1=data1.split(',')
            data1.pop()
            i=0
            print(len(data1))
            while(i<len(data1)):
                lineItem_table=LineItem()
                lineItem_table.invoice_no=meta[0]
                service=data1[i]
                i=i+1
                service=service[1:len(service)-1]
                lineItem_table.service=service
                lineItem_table.description=data1[i]
                i=i+1
                rate=data1[i]
                rate=float(rate[3:len(rate)-1])
                lineItem_table.rate=rate
                i=i+1
                lineItem_table.noHours=int(data1[i])
                i=i+1
                price=data1[i]
                price=float(price[3:len(price)-1])
                lineItem_table.price=price
                lineItem_table.save()
                i=i+1
        return HttpResponse('/advocateHome/')
    return HttpResponse('FAIL!!!!!')


def view_PDF(request):
    if request.method=="POST":
        invoice_no=request.POST.get('view_template2')
        invoice_table=Invoice.objects.get(invoice_no=invoice_no)
        user_cli=clientAccounts.objects.get(username=invoice_table.client)
        lineitem_table=LineItem.objects.filter(invoice_no=invoice_no)
        print(invoice_table.client,user_cli.first_name,lineitem_table)
    return render(request,'pdf_template.html',context={'invoice_table':invoice_table,'user_cli':user_cli,'lineitem_table':lineitem_table})

def generate_PDF(request,*args,**kwargs):
    if request.method=="POST":
        invoice_no=request.POST.get('view_template3')
        invoice_table=Invoice.objects.get(invoice_no=invoice_no)
        user_cli=clientAccounts.objects.get(username=invoice_table.client)
        lineitem_table=LineItem.objects.filter(invoice_no=invoice_no)
        print(invoice_table.client,user_cli.first_name,lineitem_table)
        context={'invoice_table':invoice_table,'user_cli':user_cli,'lineitem_table':lineitem_table}
    template=get_template('pdf_template.html')
    html=template.render(context)
    pdf=render_to_pdf('pdf_template.html',context)
    if pdf:
        response= HttpResponse(pdf,content_type='applciation/pdf')
        filename="Invoice_%s.pdf" %("12341231")
        content="inline; filename='%s'"%(filename)
        download=request.GET.get("download")
        if download:
            content="attachment; filename='%s'" %(filename)
        response['Content-Disposition']=content
        return response
    return HttpResponse("Not found")

