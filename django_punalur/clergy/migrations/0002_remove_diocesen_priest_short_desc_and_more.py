# Generated by Django 4.1.2 on 2022-10-30 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clergy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diocesen_priest',
            name='short_desc',
        ),
        migrations.RemoveField(
            model_name='relgious_priest',
            name='short_desc',
        ),
    ]
