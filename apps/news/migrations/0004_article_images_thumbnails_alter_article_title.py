# Generated by Django 4.1.3 on 2022-12-08 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='images_thumbnails',
            field=models.JSONField(default=dict, verbose_name='Images thumbnails'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=240, verbose_name='Title'),
        ),
    ]
