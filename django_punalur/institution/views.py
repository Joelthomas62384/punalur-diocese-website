from django.shortcuts import render
from . models import institution
from home.models import About
from django.contrib import messages
# Create your views here.
def institution_card(request):
    context={
        'institution':institution.objects.all(),
        'about':About.objects.all()
    }
    return render (request,'institution.html',context)

def inst(request, slug):
    institution1=institution.objects.filter(slug=slug)[0]
    context={
        'institution':institution1,
        'about':About.objects.all()
    }
    return render(request,'institutionSingle.html',context)


def search(request):
    
    about=About.objects.all()
    query=request.GET['searchBlog']


    if len(query)>70:
        insti=institution.objects.none()
    else:
                
        insti=institution.objects.filter(institution_name__icontains=query)
        
        
       

    if insti.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    content={
        'query':query,
        'institution':insti,
        'about':about
    }
    return render(request,"institutionSearch.html",content)