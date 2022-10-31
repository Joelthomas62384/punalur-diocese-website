from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path("",views.institution_card,name="posts"),
    path("search",views.search,name="Search"),
  
    path("<str:slug>",views.inst,name="posts"),


]