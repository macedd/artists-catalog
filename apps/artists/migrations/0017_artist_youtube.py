# Generated by Django 4.1.3 on 2022-12-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0016_alter_artist_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='youtube',
            field=models.CharField(blank=True, max_length=60, verbose_name='Youtube'),
        ),
    ]