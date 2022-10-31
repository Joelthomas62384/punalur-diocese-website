# Generated by Django 4.1.2 on 2022-10-31 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_downloads'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloads',
            name='file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='downloads',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]