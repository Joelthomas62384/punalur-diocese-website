# Generated by Django 4.1.2 on 2022-10-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_religious_women'),
    ]

    operations = [
        migrations.AddField(
            model_name='religious_women',
            name='image',
            field=models.ImageField(default='', upload_to='religous woman'),
            preserve_default=False,
        ),
    ]