# Generated by Django 4.2.2 on 2023-06-23 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Category safe URL'),
        ),
    ]
