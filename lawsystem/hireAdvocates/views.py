from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from advocate.models import advocateAccounts
from client.models import clientAccounts
# Create your views here.

def hireAdvocates(request): 
    return render(request,'project.html')

def criminalAd(request):
    ad_details=advocateAccounts.objects.filter(Q(expertise='criminal'))
    if request.method=="POST":
        val=request.POST['add']
        username=request.user
        id=clientAccounts.objects.get(Q(username=username))
        id.hiredAdUsername +=","+val
        id.save()
        print(id.hiredAdUsername)
    return render(request,'criminal.html',{'ad_details':ad_details})

def civilAd(request):
    ad_details=advocateAccounts.objects.filter(Q(expertise='civil'))
    return render(request,'civil.html',{'ad_details':ad_details})

def commonAd(request):
    return render(request,'common.html')

def statutoryAd(request):
    return render(request,'statutory.html')

def firms(request):
    ad_details=advocateAccounts.objects.all()
    return render(request,'firms.html',{'ad_details':ad_details})

