
from django.urls import path
from . import views

urlpatterns = [

    path("",views.news,name="news"),
    path("search",views.news_search,name="Searchnews"),
    path('newsComment',views.news_Comment,name="newsComment"),
    path("<str:slug>",views.news_post,name="posts"),


]
