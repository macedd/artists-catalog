# Generated by Django 4.1.3 on 2022-11-27 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_featured_alter_article_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=120, unique=True, verbose_name='Slug'),
        ),
    ]