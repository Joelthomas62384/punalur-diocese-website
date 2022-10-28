# Generated by Django 4.1.2 on 2022-10-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='Blog_Thumbnail',
            field=models.ImageField(default='', upload_to='post thumbnail'),
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='author_image',
            field=models.ImageField(default='', upload_to='post images'),
        ),
    ]