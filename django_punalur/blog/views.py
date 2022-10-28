from django.shortcuts import redirect, render
from . models import Blog_Post, BlogComment
from django.contrib import messages
from home.models import About

def posts(request,slug):
    about=About.objects.all()
    blog=Blog_Post.objects.filter(slug=slug)[0]
    comments=BlogComment.objects.filter(post=blog).order_by('-timestamp')
    comentlen=len(comments)
    context={
        'blog_posts':blog,
        'about':about,
        'comments':comments,
        'commentlen':comentlen
    }
    return render(request,'single.html',context)

def blog(request):
    blog=Blog_Post.objects.all().order_by('-Time_stamp')
    about=About.objects.all()
    context={
        'blog':blog,
        'about':about
    }
    return render(request,'blog.html',context)

def search(request):
    about=About.objects.all()
    query=request.GET['searchBlog']


    if len(query)>70:
        posts=Blog_Post.objects.none()
    else:
                
        posts_title=Blog_Post.objects.filter(title__icontains=query)
        content_posts=Blog_Post.objects.filter(content__icontains=query)
        short_description_posts=Blog_Post.objects.filter(short_description__icontains=query)
        serial_no_posts=Blog_Post.objects.filter(serial_no__icontains=query)
        Time_stamp_posts=Blog_Post.objects.filter(Time_stamp__icontains=query)
        author_posts=Blog_Post.objects.filter(author__icontains=query)
        posts=posts_title.union(content_posts,short_description_posts,short_description_posts,serial_no_posts,Time_stamp_posts,author_posts).order_by('-Time_stamp')

    if posts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    content={
        'query':query,
        'posts':posts,
        'about':about
    }
    return render(request,"blogSearch.html",content)

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get('comment')
        username=request.POST.get('nameComment')
        postSno =request.POST.get('postSno')
        post= Blog_Post.objects.get(serial_no=postSno)
        comment=BlogComment(comment= comment, username=username, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
    return redirect(f"/blog/{post.slug}")

