from django.shortcuts import render
from . models import Diocesen_Priest, Relgious_Priest
from home.models import About
from django.contrib import messages

# Create your views here.
def priests(request):
    about=About.objects.all()
    context={
        'about':about
    }
    return render(request,'priest.html',context)

def diocesen_priest(request):
    clergy_card=Diocesen_Priest.objects.all().order_by('name')
    about=About.objects.all()
    context={
        'clergy':clergy_card,
        'about':about
    }
    return render(request,'diocesenClergy.html',context)

def search(request):
    about=About.objects.all()
    # query2=[]
    # for i in range(3):
    #     query2.append(query1)
    # for i in range(len(query)):
    #     query=f"{query2[i]}+"
        
    query=request.GET['priestSearch']
    

    if len(query)>70:
        priests=Diocesen_Priest.objects.none()
    else:
                
        dpriest_name=Diocesen_Priest.objects.filter(name__icontains=query)
        address=Diocesen_Priest.objects.filter(Address__icontains=query)
        seo=Diocesen_Priest.objects.filter(seo__icontains=query)
        priests=dpriest_name.union(address,seo)
       
        # posts=posts_title.union(content_posts,short_description_posts,short_description_posts,serial_no_posts,Time_stamp_posts,author_posts).order_by('-Time_stamp')

    if priests.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    content={
        'query':query,
        'clergy':priests,
        'about':about
    }
    print(priests)
    return render(request,"DiocesanClergySearch.html",content)