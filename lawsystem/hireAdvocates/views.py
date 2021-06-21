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
        id.hiredAdUsername =val
        id.save()
        print(id.hiredAdUsername)
    return render(request,'criminal.html',{'ad_details':ad_details})

def civilAd(request):
    ad_details=advocateAccounts.objects.filter(Q(expertise='civil'))
    if request.method=="POST":
        val=request.POST['add']
        username=request.user
        id=clientAccounts.objects.get(Q(username=username))
        id.hiredAdUsername =val
        id.save()
        print(id.hiredAdUsername)
    return render(request,'civil.html',{'ad_details':ad_details})
    
def firms(request):
    ad_details=advocateAccounts.objects.all()
    if request.method=="POST":
        val=request.POST['add']
        username=request.user 
        id=clientAccounts.objects.get(Q(username=username))
        id.hiredAdUsername =val
        id.save()
        print(id.hiredAdUsername)
    return render(request,'firms.html',{'ad_details':ad_details})


def MyAdList(request):
    if request.method=="POST":
        user=clientAccounts.objects.get(username=request.user)
        user.hiredAdUsername=""
        user.save()
        return render(request,'MyAdList.html')
    else:
        user=clientAccounts.objects.get(username=request.user)
        hiredAdUsername=user.hiredAdUsername
        if hiredAdUsername:
            adList=advocateAccounts.objects.get(username=hiredAdUsername)
            print("adlist=====")
            print(adList.username)
            return render(request,'MyAdList.html',{'id':adList})
        else:
            return render(request,'MyAdList.html')
        
def MyClientList(request):
    return render(request,'MyClientList.html')