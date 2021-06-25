from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from advocate.models import advocateAccounts
from client.models import clientAccounts
# Create your views here.

def hireAdvocates(request): 
    return render(request,'project.html')

#common function for adding advocate name to clients table and vice versa
def addAdvocate(val,username):
    print(val,username)
    id=clientAccounts.objects.get(Q(username=username))
    if val not in id.hiredAdUsername and val not in id.confirmedAds:
        ad_user=advocateAccounts.objects.get(Q(username=val))
        print(ad_user.clientRequest)
        if id.username not in ad_user.clientRequest:
            ad_user.clientRequest+=id.username+","
            ad_user.save()
        id.hiredAdUsername += val+"," 
        ad_user.save()
    id.save()
    print(id.hiredAdUsername)

def criminalAd(request):
    ad_details=advocateAccounts.objects.filter(Q(expertise='criminal'))
    if request.method=="POST":
        val=request.POST['add']
        username=request.user
        addAdvocate(val,username)
    return render(request,'criminal.html',{'ad_details':ad_details})

def civilAd(request):
    ad_details=advocateAccounts.objects.filter(Q(expertise='civil'))
    if request.method=="POST":
        val=request.POST['add']
        username=request.user
        addAdvocate(val,username)
    return render(request,'civil.html',{'ad_details':ad_details})
    
def firms(request):
    ad_details=advocateAccounts.objects.all()
    if request.method=="POST":
        val=request.POST['add']
        username=request.user
        addAdvocate(val,username)
    return render(request,'firms.html',{'ad_details':ad_details})

#common function for displaying hired advocates details to clients
def displayHiredAds(req_user):
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
        usernameList=displayHiredAds(req_user)
        return render(request,'MyAdList.html',{'usernameList':usernameList})
    else:
        user=clientAccounts.objects.get(username=request.user)
        if user.hiredAdUsername:
            req_user=request.user
            usernameList=displayHiredAds(req_user)
            return render(request,'MyAdList.html',{'usernameList':usernameList})
        else:
            return render(request,'MyAdList.html')
        
def confirmedAds(request):
    user_cli=clientAccounts.objects.get(username=request.user)
    confirmedAds=user_cli.confirmedAds
    usernameList=[]
    if confirmedAds:
        l=confirmedAds.split(',')
        l.pop()
        for i in l:
            usernameList.append(advocateAccounts.objects.get(username=i))
        print(usernameList)
    return render(request,'confirmedAds.html',{'usernameList':usernameList})    

#confirmedClients List
def MyClientList(request):
    user_ad=advocateAccounts.objects.get(username=request.user)
    confirmedClients=user_ad.confirmedClients
    usernameList=[]
    if confirmedClients:
        l=confirmedClients.split(',')
        l.pop()
        for i in l:
            usernameList.append(clientAccounts.objects.get(username=i))
        print(usernameList)
    return render(request,'MyClientList.html' ,{'usernameList':usernameList})

def clientRequests(request):
    user_ad=advocateAccounts.objects.get(username=request.user)
    clientRequest=user_ad.clientRequest
    usernameList1=[]
    if request.method=="POST":
        cli_add=request.POST['add']
        user_cli=clientAccounts.objects.get(username=cli_add)
        if clientRequest:
            #remove from advocate->clientRequest
            l=clientRequest.split(',')
            l.remove(cli_add)
            user_ad.clientRequest=",".join(l)
            print(user_ad.clientRequest)
            #remove client-> mylist(hiredAdUsername)
            l=user_cli.hiredAdUsername.split(',')
            l.remove(user_ad.username)
            user_cli.hiredAdUsername=",".join(l)
            print(user_cli.hiredAdUsername)
            user_cli.save()
            user_ad.save()
            #add in advocate->mylist(confirmedClients)
            if user_ad.confirmedClients:
                user_ad.confirmedClients+=user_cli.username+","
            else:
                user_ad.confirmedClients=user_cli.username+","
            print(user_ad.confirmedClients)
            #add in client->confirmedAds
            if user_cli.confirmedAds:
                user_cli.confirmedAds+=user_ad.username+","
            else:
                user_cli.confirmedAds=user_ad.username+","
            print(user_cli.confirmedAds)
        user_cli.save()
        user_ad.save()
    if clientRequest:
        l=clientRequest.split(',')
        l.pop()
        for i in l:
            usernameList1.append(clientAccounts.objects.get(username=i))
        usernameList=usernameList1
        render(request,'clientRequests.html',{'usernameList':usernameList})
    return render(request,'clientRequests.html',{'usernameList':usernameList1})