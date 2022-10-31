from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path("",views.priests,name="posts"),
    path("diocesanPriest",views.diocesen_priest,name="diocesenPriest"),
    path("religiousPriest",views.religious_Priest,name="diocesenPriest"),
    path("search",views.search,name="Search"),
    path("searchReligious",views.search_relgious,name="SearchRelgious"),
    # # path('postComment',views.postComment,name="postComment"),
    # path("<str:slug>",views.minis,name="posts"),


]