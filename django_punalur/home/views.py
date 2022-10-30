from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import About, Bishop, Contact, bibleverse, bishopschedule, bishopvenue, carouselimg
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




# def blog(request):

#     about=About.objects.all()
#     blog=Blog_Post.objects.all()
  
    
    # content={
    #     'about':about,
    #     'blog':blog,
        
    # }
    # return render(request,"blog.html",content)



# def News(request):
#     about=About.objects.all()
#     content={
#         'about':about
#     }
#     return render (request, "News.html",content)




# def news_single(request):
#     pass


# def blog_search(request):
    
#     query=request.GET['searchBlog']

#     if len(query)>70:
#         posts=Blog_Post.objects.none()
#     else:
                
#         posts_title=Blog_Post.objects.filter(title__icontains=query)
#         content_posts=Blog_Post.objects.filter(content__icontains=query)
#         short_description_posts=Blog_Post.objects.filter(short_description__icontains=query)
#         serial_no_posts=Blog_Post.objects.filter(serial_no__icontains=query)
#         Time_stamp_posts=Blog_Post.objects.filter(Time_stamp__icontains=query)
#         author_posts=Blog_Post.objects.filter(author__icontains=query)
#         posts=posts_title.union(content_posts,short_description_posts,short_description_posts,serial_no_posts,Time_stamp_posts,author_posts)

#     if posts.count()==0:
#         messages.warning(request, "No search results found. Please refine your query.")
#     content={
#         'query':query,
#         'posts':posts
#     }
#     return render(request,"blogSearch.html",content)

# def postComment(request):
#     if request.method=="POST":
#         comment=request.POST.get('comment')
#         username=request.POST.get('nameComment')
#         postSno =request.POST.get('postSno')
#         post= Blog_Post.objects.get(sno=postSno)
#         comment=BlogComment(comment= comment, username=username, post=post)
#         comment.save()
#         messages.success(request, "Your comment has been posted successfully")

        

    