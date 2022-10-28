from django.db import models
from django.utils.timezone import now


# Create your models here.
class Blog_Post(models.Model):
    serial_no=models.AutoField(primary_key=True)
    title=models.CharField(max_length=10000)
    slug=models.CharField(max_length=10000,verbose_name="title(use '-' instead of space and -blog at the end)")
    
    author=models.CharField(max_length=10000)
    author_image=models.ImageField(upload_to="postimages",default="")
    Blog_Thumbnail=models.ImageField(upload_to="post thumbnail",default="")
    Time_stamp=models.DateTimeField(blank=True)
    short_description=models.TextField(default="")
    content=models.TextField()

    def __str__(self) -> str:
        return self.title + " by "+self.author

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    username=models.CharField(max_length=1000)
    post=models.ForeignKey(Blog_Post, on_delete=models.CASCADE)
    
    timestamp= models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.comment[0:15]+"... by "+ self.username

