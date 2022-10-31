from django.db import models

# Create your models here.

class institution(models.Model):
    institution_name=models.CharField(max_length=1000)
    slug=models.CharField(max_length=1000,default="")
    thumbnail=models.ImageField(upload_to='ministries')
    content=models.TextField()

    def __str__(self) -> str:
        return self.institution_name