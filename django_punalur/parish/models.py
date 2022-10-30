from django.db import models

# Create your models here.
from django.db import models



class parish(models.Model):
    parish_name=models.CharField(max_length=1000)
    slug=models.CharField(max_length=1000,default="")
    patron=models.CharField(max_length=1000,default="")
    place=models.CharField(max_length=1000,default="")
    keywords=models.CharField(max_length=1000,default="")

    thumbnail=models.ImageField(upload_to='parishes')
    content=models.TextField()

    def __str__(self) -> str:
        return self.parish_name