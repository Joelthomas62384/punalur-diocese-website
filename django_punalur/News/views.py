from django.shortcuts import redirect, render
from home.models import About
from . models import news_Post, newsComment
from django.contrib import messages

# Create your views here.

def news(request):
    about=About.objects.all()
    news=news_Post.objects.all().order_by('-Time_stamp')
    context={
        'about':about,
        'news':news

    }

    return render (request,'News.html',context)



def news_search(request):
    about=About.objects.all()
    query=request.GET['searchNews']
    if len(query)>80:
        news=news_Post.objects.none()
    else:
        title_news=news_Post.objects.filter(title__icontains=query)
        author_news=news_Post.objects.filter(author__icontains=query)
        short_news=news_Post.objects.filter(short_description__icontains=query)
        content_news=news_Post.objects.filter(content__icontains=query)
        news=title_news.union(author_news,short_news,content_news).order_by('-Time_stamp')
    if news.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    content={
        'query':query,
        'posts':news,
        'about':about
    }
    return render(request,"newsSearch.html",content)








def news_post(request,slug):
    news_pst=news_Post.objects.filter(slug=slug)[0]
    comments=newsComment.objects.filter(news_post=news_pst).order_by('-timestamp')
    
    commentlen=len(comments)
    
    context={
        'news_post': news_pst,
        'comments':comments,
        "commentlen":commentlen

    }
    return render (request,'newsSingle.html',context)
    




def news_Comment(request):
    if request.method=="POST":
        comment=request.POST.get('comment')
        username=request.POST.get('nameComment')
        postSno =request.POST.get('postSno')
        post= news_Post.objects.get(serial_no=postSno)
        comment=newsComment(comment= comment, username=username, news_post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")

    return redirect(f"/News/{post.slug}",'#comments')
