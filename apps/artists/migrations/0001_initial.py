# Generated by Django 4.0.6 on 2022-07-27 05:25

import artists.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('title', models.CharField(max_length=60)),
                ('featured', models.BooleanField()),
                ('photo', models.ImageField(upload_to=artists.models.artist_directory_path)),
                ('biography', models.TextField()),
                ('birth_date', models.DateField()),
                ('birth_city', models.CharField(max_length=120)),
                ('artistic_kinship', models.TextField()),
                ('groups_affiliation', models.TextField()),
                ('works', models.TextField()),
                ('website', models.CharField(max_length=120)),
                ('instagram', models.CharField(max_length=60)),
                ('facebook', models.CharField(max_length=60)),
                ('whatsapp', models.CharField(max_length=60)),
                ('views', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]