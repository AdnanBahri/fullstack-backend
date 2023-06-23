# Generated by Django 4.2.2 on 2023-06-23 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_productcolor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Category safe URL'),
        ),
    ]
