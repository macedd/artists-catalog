# Generated by Django 4.1 on 2022-09-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0008_remove_artist_original_slug_artist_past_slugs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='past_slugs',
            field=models.JSONField(default=list, verbose_name='Past Slugs'),
        ),
    ]
