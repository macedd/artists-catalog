# Generated by Django 4.1.6 on 2023-03-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0017_artist_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='images_thumbnails',
            field=models.JSONField(default=dict, verbose_name='Images thumbnails'),
        ),
    ]
