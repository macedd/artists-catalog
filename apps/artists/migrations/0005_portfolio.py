# Generated by Django 4.0.6 on 2022-07-29 02:48

import artists.fields
import artists.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_alter_category_options_artist_related_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('upload_type', models.CharField(choices=[('music', 'Music'), ('drawing', 'Drawing'), ('photo', 'Photo'), ('video', 'Video')], max_length=10)),
                ('upload', artists.fields.PortfolioUploadField(blank=True, null=True, upload_to=artists.models.artist_directory_path)),
                ('link', models.URLField(blank=True, null=True)),
                ('views', models.IntegerField(default=0, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.artist')),
            ],
        ),
    ]
