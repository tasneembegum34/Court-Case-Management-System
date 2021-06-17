from django.shortcuts import render
from django.db.models import Q
from advocate.models import advocateAccounts
# Create your views here.

def hireAdvocates(request): 
    return render(request,'project.html')

def criminalAd(request):
    ad_details=advocateAccounts.objects.filter(Q(expertise='criminal'))
    for i in ad_details:
        print(i.first_name,i.last_name,i.phno)
    return render(request,'criminal.html',{'ad_details':ad_details})

def civilAd(request):
    return render(request,'civil.html')

def commonAd(request):
    return render(request,'common.html')

def statutoryAd(request):
    return render(request,'statutory.html')

def firms(request):
    return render(request,'firms.html')