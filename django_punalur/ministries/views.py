from django.shortcuts import render
from . models import ministry
from home.models import About
from django.contrib import messages




def minis(request,slug):
    about=About.objects.all()
    min=ministry.objects.filter(slug=slug)[0]
    context={
        'minis':min,
        'about':about
    }
    return render(request,'ministrySingle.html',context)


def ministry_card(request):
    about=About.objects.all()
    ministries_card=ministry.objects.all()
    context={
        'about':about,
        'ministry':ministries_card
    }
    return render(request,"gallery.html",context)

def search(request):
    
    about=About.objects.all()
    query=request.GET['searchBlog']


    if len(query)>70:
        minis=ministry.objects.none()
    else:
                
        minis=ministry.objects.filter(ministry_name__icontains=query)
        
        
       

    if minis.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    content={
        'query':query,
        'minis':minis,
        'about':about
    }
    return render(request,"minisSearch.html",content)

