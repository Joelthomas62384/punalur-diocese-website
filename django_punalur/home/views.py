from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import About, Bishop, Contact, Religious_Women, bibleverse, bishopschedule, bishopvenue, carouselimg, downloads
from datetime import datetime
from django.contrib import messages
from News.models import news_Post

now = datetime.now()

current_time = now.strftime("%H:%M:%S")


# Create your views here.
def home(request):
    about=About.objects.all()
    news=news_Post.objects.all().order_by('-Time_stamp')
    ima=carouselimg.objects.all()
    bp=Bishop.objects.all()
    bs=bishopschedule.objects.all()
    bv=bishopvenue.objects.all()
    bible=bibleverse.objects.all()
    about=About.objects.all()
    
  
  

    num=range(len(ima))

    carousals={
        'ima':ima,
        'num':num,
        'bp':bp,
        'bs':bs,
        'bv':bv,
        'bible':bible,
        'about':about,
        'news':news
        
      
    }
    return render(request,"index.html",carousals)




def about(request):

    about=About.objects.all()
    content={
        'about':about
    }
    return render(request,"About.html",content)



# def blog_single(request,slug):
#     about=About.objects.all()
#     blogpsts=Blog_Post.objects.filter(slug=slug)[0]
#     comments=BlogComment.objects.filter(post=blogpsts)
  
    
    # content={
    #     'about':about,
    #     'blog_posts':blogpsts,
    #     'comments':comments
    # }
    # return render(request,"single.html",content)



def diocese(request):
    about=About.objects.all()
    content={
        'about':about
    }
    return render (request,"diocese.html",content)

def religious_women(request):
    religious_woman=Religious_Women.objects.all().order_by('Congrigation')
    about=About.objects.all()
    context={
        'rewo':religious_woman,
        'about':about
    }
    return render(request,'religiousWomen.html',context)







def contact(request):
    about=About.objects.all()
    content={
        'about':about
    }
    if request.method=="POST":
        name=request.POST['userName']
        email=request.POST['userEmail']
        phone=request.POST['userPhone']
        msg=request.POST['userMsg']
        if len(name)<1 or len(email)<3 or len(phone)<5 or len(content)<1:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name_of_person=name,email=email,phone=phone,subject=msg)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request,"contact.html",content)




def search(request):
    about=About.objects.all()
   
        
    query=request.GET['priestSearch']
    print("This is the empty",query)
    

    if len(query)>70:
        convent=Religious_Women.objects.none()
    else:
                
        house_name=Religious_Women.objects.filter(name__icontains=query)
        address=Religious_Women.objects.filter(Address__icontains=query)
        seo=Religious_Women.objects.filter(seo__icontains=query)
        Congrigation=Religious_Women.objects.filter(Congrigation__icontains=query)
        convent=house_name.union(address,seo,Congrigation)
       
        # posts=posts_title.union(content_posts,short_description_posts,short_description_posts,serial_no_posts,Time_stamp_posts,author_posts).order_by('-Time_stamp')

    if convent.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    content={
        'query':query,
        'convent':convent,
        'about':about
    }
    return render(request,"relgiousWomenSearch.html",content)

def download(request):
    context={
        'download':downloads.objects.all(),
        'about':About.objects.all()
    }
    return render(request,'downloads.html',context)