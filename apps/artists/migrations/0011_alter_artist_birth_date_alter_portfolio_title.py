# Generated by Django 4.1.1 on 2022-10-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0010_category_created_at_category_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='birth_date',
            field=models.DateField(blank=True, verbose_name='Birth date'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(blank=True, max_length=120, verbose_name='Title'),
        ),
    ]
