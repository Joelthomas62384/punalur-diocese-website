# Generated by Django 4.1.2 on 2022-10-26 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_blog_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='author_image',
            field=models.ImageField(default='', upload_to='postimages'),
        ),
    ]
