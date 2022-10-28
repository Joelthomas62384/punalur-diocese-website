from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path("",views.blog,name="posts"),
    path("search",views.search,name="Search"),
    path('postComment',views.postComment,name="postComment"),
    path("<str:slug>",views.posts,name="posts"),


]
