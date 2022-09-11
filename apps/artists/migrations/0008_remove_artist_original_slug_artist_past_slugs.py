# Generated by Django 4.1 on 2022-09-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0007_artist_original_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='original_slug',
        ),
        migrations.AddField(
            model_name='artist',
            name='past_slugs',
            field=models.JSONField(default=[], verbose_name='Past Slugs'),
        ),
    ]