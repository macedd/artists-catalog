# Generated by Django 4.1.3 on 2022-11-27 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0011_alter_artist_birth_date_alter_portfolio_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='past_slugs',
            field=models.JSONField(default=list, verbose_name='Past Slugs'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=120, unique=True, verbose_name='Slug'),
        ),
    ]