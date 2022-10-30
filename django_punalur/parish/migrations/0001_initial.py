# Generated by Django 4.1.2 on 2022-10-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministry_name', models.CharField(max_length=1000)),
                ('slug', models.CharField(default='', max_length=1000)),
                ('thumbnail', models.ImageField(upload_to='parishes')),
                ('content', models.TextField()),
            ],
        ),
    ]
