# Generated by Django 4.1.2 on 2022-10-26 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_blogcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Blog_Post',
        ),
        migrations.DeleteModel(
            name='BlogComment',
        ),
    ]
