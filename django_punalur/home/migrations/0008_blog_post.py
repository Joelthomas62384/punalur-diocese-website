# Generated by Django 4.1.2 on 2022-10-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contact_time_of_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Post',
            fields=[
                ('serial_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=10000)),
                ('author', models.CharField(max_length=10000)),
                ('author_image', models.ImageField(upload_to='post_images')),
                ('Time_stamp', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
