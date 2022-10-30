from django.shortcuts import render
from . models import parish
from home.models import About
from django.contrib import messages

# Create your views here.

def parish_card(request):
    about=About.objects.all()
    parish_name=parish.objects.all()
    content={
        'about':about,
        'parish':parish_name
    }

    return render(request,'parish.html',content)

def search(request):
    about=About.objects.all()
    query=request.GET['searchParish']


    if len(query)>70:
        parish_card=parish.objects.none()
    else:
                
        parish_name=parish.objects.filter(parish_name__icontains=query)
        patron=parish.objects.filter(patron__icontains=query)
        place=parish.objects.filter(place__icontains=query)
        keywords=parish.objects.filter(keywords__icontains=query)
        content=parish.objects.filter(content__icontains=query)
       
        parish_card=parish_name.union(content,parish_name,patron,place,keywords)
    if parish_card.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    content={
        'query':query,
        'parish':parish_card,
        'about':about
    }
    print(parish_card)
    return render(request,"parishSearch.html",content)

def about_parish(request,slug):
    parish_about=parish.objects.filter(slug=slug)[0]
    about=About.objects.all()

    content={
        'parish':parish_about,
        'about':about
    }
  

    return render(request,'parishSingle.html',content)