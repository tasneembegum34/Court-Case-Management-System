from django.shortcuts import render
from advocate.models import advocateAccounts
from client.models import clientAccounts
# Create your views here.

def generateInvoice(request):
    cli_name=request.POST['generate_invoice']
    user_cli=clientAccounts.objects.get(username=cli_name)
    user_ad=advocateAccounts.objects.get(username=request.user)
    return render(request,'editableinvoice.html',context={'user_cli':user_cli,'user_ad':user_ad})