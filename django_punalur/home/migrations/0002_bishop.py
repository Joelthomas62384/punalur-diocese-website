# Generated by Django 4.1.2 on 2022-10-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bishop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(default='', max_length=5000)),
                ('bimage', models.ImageField(upload_to='Bishopdata')),
                ('bdata', models.TextField()),
            ],
        ),
    ]
