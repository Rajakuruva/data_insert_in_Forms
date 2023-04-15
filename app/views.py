from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from app.models import *

def Insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        print(request.POST)
        return HttpResponse("Data submitted succesffully Comleted")

    return render(request,'Insert_topic.html')

def Insert_webpage(request):
    tlo=Topic.objects.all()
    d={'topi':tlo}
    if request.method=='POST':
        tn=request.POST['topic']
        nm=request.POST['na']
        urs=request.POST['ur']
        ems=request.POST['em']
        to=Topic.objects.get(topic_name=tn)
        wo=Webpage.objects.get_or_create(topic_name=to,name=nm,url=urs,email=ems)[0]
        wo.save()
        return HttpResponse("Data is submitted!!!")

    return render(request,'Insert_webpage.html',d)

def Insert_Access(request):
    
    wlo=Webpage.objects.all()
    d={'webs':wlo}
    if request.method=='POST':
        nam=request.POST['name']
        au=request.POST['aut']
        dat=request.POST['dat']
        wo=Webpage.objects.get(name=nam)
        ao=AccessRecord.objects.get_or_create(name=wo,author=au,dete=dat)[0]
        ao.save()
        return HttpResponse("Data submitted successfully!!!")
    return render(request,'Insert_Access.html',d)
def Retrieve_Topic(request):
    two=Topic.objects.all()
    d={'topic':two}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        topicquery=Webpage.objects.none()
        for i in td:
            topicquery=topicquery|Webpage.objects.filter(topic_name=i)
        d1={'top':topicquery}
        return render(request,'Display_data.html',d1)
        

    return render(request,'Retrieve_Topic.html',d)

def Retrieve_Acess(request):
    wlo=Webpage.objects.all()
    d={'webs':wlo}
    if request.method=='POST':
        no=request.POST.getlist('nm')
        emptyweb=AccessRecord.objects.none()
        for x in no:
            emptyweb=emptyweb|AccessRecord.objects.filter(name=x)
        d1={'acess':emptyweb}
        return render(request,'Display_Acess.html',d1)

    return render(request,'Retrieve_Acess.html',d)

def Checkbox(request):
    tlo=Topic.objects.all()
    d={'topic':tlo}
    return render(request,'Checkbox.html',d)

def Checkbox1(request):
    wlo=Webpage.objects.all()
    d={'webs':wlo}

    return render(request,'Checkbox1.html',d)