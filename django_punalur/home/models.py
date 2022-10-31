

from django.db import models
from django.utils.timezone import now
from django import forms




# Create your models here.
class carouselimg(models.Model):
    title=models.CharField(max_length=500,default="")
    newimage=models.ImageField(upload_to="carouselimg")

    def __str__(self) -> str:
        return self.title
class Bishop(models.Model):
    bname=models.CharField(max_length=5000,default="")
    bimage=models.ImageField(upload_to="Bishopdata")
    bdata=models.TextField()
    
    def __str__(self) -> str:
        return self.bname

class bishopschedule(models.Model):
    frm=models.DateField()
    to=models.DateField()
    month=models.CharField(max_length=5000,default="")

    def __str__(self) -> str:
        return self.month

class bishopvenue(models.Model):
    venue=models.CharField(max_length=5000,default="")
    datex=models.CharField(max_length=5000,default="")
    month=models.ForeignKey("bishopschedule", verbose_name="month", on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.venue

class bibleverse(models.Model):
    versus=models.CharField(max_length=5000)
    reference=models.CharField(max_length=5000)

    def __str__(self) -> str:
        return self.reference


class About(models.Model):
    short_desc=models.TextField(default="")
    about_diocese=models.TextField(default="")

    def __str__(self) -> str:
        return "About Punalur Diocese"

class Contact(models.Model):
    name_of_person=models.CharField(max_length=10000)
    email=models.EmailField(max_length=10000)
    phone=models.CharField(max_length=10000)
    subject=models.TextField()
    time_of_entry=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self) -> str:
        return self.name_of_person



class Religious_Women(models.Model):
    serial_number=models.AutoField(primary_key=True)
    name=models.CharField(max_length=1000,default="")
    seo=models.CharField(max_length=10000,default="")
    Congrigation=models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to="religous woman")
    Patron=models.CharField(max_length=200,default="")
    Phone_Number=models.CharField(max_length=200,default="")
    Email_Id=models.CharField(max_length=200,default="")
    Address=models.CharField(max_length=20000,default="")
    

    def __str__(self) -> str:
        return self.name
class downloads(models.Model):
    title = models.CharField(max_length=5500, default="")
    file = models.FileField(upload_to="downloads",max_length=100000)

    def __str__(self) -> str:
        return self.title

