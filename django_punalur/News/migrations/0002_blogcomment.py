# Generated by Django 4.1.2 on 2022-10-28 01:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('username', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('news_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.news_post')),
            ],
        ),
    ]
