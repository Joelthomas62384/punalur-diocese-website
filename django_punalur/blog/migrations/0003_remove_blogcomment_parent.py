# Generated by Django 4.1.2 on 2022-10-27 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
    ]
