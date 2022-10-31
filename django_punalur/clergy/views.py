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

def religious_Priest(request):
    #     serial_number=models.AutoField(primary_key=True)
    # name=models.CharField(max_length=1000,default="")
    # seo=models.CharField(max_length=10000,default="")
    # Congrigation=models.CharField(max_length=200,default="")
    # image=models.ImageField(upload_to="priest")
    # Date_of_Birth=models.CharField(max_length=200,default="")
    # Date_of_Ordination=models.CharField(max_length=200,default="")
    # Date_of_Feast=models.CharField(max_length=200,default="")
    # Phone_Number=models.CharField(max_length=200,default="")
    # Email_Id=models.CharField(max_length=200,default="")
    # Address=models.CharField(max_length=20000,default="")
    # .values('Congrigation', 'name','Date_of_Birth','image','Date_of_Ordination','Date_of_Feast','Phone_Number','Email_Id','Address')
    clergy_card=Relgious_Priest.objects.all().order_by('Congrigation')
    about=About.objects.all()
    context={
        'clergy':clergy_card,
        'about':about
    }
    return render(request,'religiousClergy.html',context)

def search_relgious(request):
    about=About.objects.all()
    # query2=[]
    # for i in range(3):
    #     query2.append(query1)
    # for i in range(len(query)):
    #     query=f"{query2[i]}+"
        
    query=request.GET['priestSearch']
    print("This is the empty",query)
    

    if len(query)>70:
        priests=Relgious_Priest.objects.none()
    else:
                
        dpriest_name=Relgious_Priest.objects.filter(name__icontains=query)
        address=Relgious_Priest.objects.filter(Address__icontains=query)
        seo=Relgious_Priest.objects.filter(seo__icontains=query)
        Congrigation=Relgious_Priest.objects.filter(Congrigation__icontains=query)
        priests=dpriest_name.union(address,seo,Congrigation)
       
        # posts=posts_title.union(content_posts,short_description_posts,short_description_posts,serial_no_posts,Time_stamp_posts,author_posts).order_by('-Time_stamp')

    if priests.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    content={
        'query':query,
        'clergy':priests,
        'about':about
    }
    return render(request,"religiousPriestSearch.html",content)