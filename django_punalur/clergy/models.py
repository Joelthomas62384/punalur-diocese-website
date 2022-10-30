from django.db import models

# Create your models here.

class Diocesen_Priest(models.Model):
    serial_number=models.AutoField(primary_key=True)
    name=models.CharField(max_length=1000,default="")
    seo=models.CharField(max_length=10000,default="")
    image=models.ImageField(upload_to="priest")
    Date_of_Birth=models.CharField(max_length=200,default="")
    Date_of_Ordination=models.CharField(max_length=200,default="")
    Date_of_Feast=models.CharField(max_length=200,default="")
    Phone_Number=models.CharField(max_length=200,default="")
    Email_Id=models.CharField(max_length=200,default="")
    Address=models.CharField(max_length=20000,default="")
    

    def __str__(self) -> str:
        return self.name



class Relgious_Priest(models.Model):
    serial_number=models.AutoField(primary_key=True)
    name=models.CharField(max_length=1000,default="")
    seo=models.CharField(max_length=10000,default="")
    Congrigation=models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to="priest")
    Date_of_Birth=models.CharField(max_length=200,default="")
    Date_of_Ordination=models.CharField(max_length=200,default="")
    Date_of_Feast=models.CharField(max_length=200,default="")
    Phone_Number=models.CharField(max_length=200,default="")
    Email_Id=models.CharField(max_length=200,default="")
    Address=models.CharField(max_length=20000,default="")
    

    def __str__(self) -> str:
        return self.name
