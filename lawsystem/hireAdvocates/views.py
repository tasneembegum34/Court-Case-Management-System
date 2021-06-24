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
        if val not in id.hiredAdUsername:
            ad_user=advocateAccounts.objects.get(Q(username=val))
            print(ad_user.clientRequest)
            if id.username not in ad_user.clientRequest:
                ad_user.clientRequest+=id.username+","
                ad_user.save()
            id.hiredAdUsername += val+"," 
        id.save()
        print(id.hiredAdUsername)
    return render(request,'criminal.html',{'ad_details':ad_details})

def civilAd(request):
    ad_details=advocateAccounts.objects.filter(Q(expertise='civil'))
    if request.method=="POST":
        val=request.POST['add']
        username=request.user
        id=clientAccounts.objects.get(Q(username=username))
        if val not in id.hiredAdUsername:
            ad_user=advocateAccounts.objects.get(Q(username=val))
            print(ad_user.clientRequest)
            if id.username not in ad_user.clientRequest:
                ad_user.clientRequest+=id.username+","
                ad_user.save()
            id.hiredAdUsername += val+"," 
        id.save()
        print(id.hiredAdUsername)
    return render(request,'civil.html',{'ad_details':ad_details})
    
def firms(request):
    ad_details=advocateAccounts.objects.all()
    if request.method=="POST":
        val=request.POST['add']
        username=request.user
        id=clientAccounts.objects.get(Q(username=username))
        if val not in id.hiredAdUsername:
            ad_user=advocateAccounts.objects.get(Q(username=val))
            print(ad_user.clientRequest)
            if id.username not in ad_user.clientRequest:
                ad_user.clientRequest+=id.username+","
                ad_user.save()
            id.hiredAdUsername += val+"," 
        id.save()
        print(id.hiredAdUsername)
    return render(request,'firms.html',{'ad_details':ad_details})


def display(req_user):
    user=clientAccounts.objects.get(username=req_user)
    hiredAdUsernames=user.hiredAdUsername
    if hiredAdUsernames:
        adlist=hiredAdUsernames.split(',')
        adlist.pop() 
        print(adlist)
        usernameList=[]
        for i in adlist:
            usernameList.append(advocateAccounts.objects.get(username=i))
        return usernameList
            
def MyAdList(request):
    if request.method=="POST"  and 'remove' in request.POST:
        req_user=request.user
        user_cli=clientAccounts.objects.get(username=req_user)
        ad_remove=request.POST['remove']
        user_ad=advocateAccounts.objects.get(username=ad_remove)
        if user_cli.hiredAdUsername:
            print(user_cli.hiredAdUsername)
            l=user_cli.hiredAdUsername.split(',')
            l.remove(ad_remove)            
            user_cli.hiredAdUsername=",".join(l)

            l2=user_ad.clientRequest.split(',')
            l2.remove(user_cli.username)
            user_ad.clientRequest=",".join(l2)

            print(user_cli.hiredAdUsername)
            print(user_ad.clientRequest)
        else:
            user_cli.hireAdUsername=""
        user_cli.save()
        user_ad.save()
        usernameList=display(req_user)
        return render(request,'MyAdList.html',{'usernameList':usernameList})
    else:
        user=clientAccounts.objects.get(username=request.user)
        if user.hiredAdUsername:
            req_user=request.user
            usernameList=display(req_user)
            return render(request,'MyAdList.html',{'usernameList':usernameList})
        else:
            return render(request,'MyAdList.html')
        
def MyClientList(request):
    return render(request,'MyClientList.html')

def clientRequests(request):
    user_ad=advocateAccounts.objects.get(username=request.user)
    clientRequest=user_ad.clientRequest
    print(user_ad.clientRequest)
    if clientRequest:
        l=clientRequest.split(',')
        print(l)
        l.pop()
        usernameList=[]
        for i in l:
            usernameList.append(clientAccounts.objects.get(username=i))
        print(usernameList[0].username)
        render(request,'clientRequests.html',{'usernameList':usernameList})
    return render(request,'clientRequests.html')