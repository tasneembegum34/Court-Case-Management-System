from django.shortcuts import render
from django.db.models import Q
from advocate.models import advocateAccounts
# Create your views here.

def hireAdvocates(request): 
    return render(request,'project.html')

def criminalAd(request):
    ad_details=advocateAccounts.objects.filter(Q(expertise='criminal'))
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