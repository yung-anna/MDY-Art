# Generated by Django 2.2.5 on 2020-02-21 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other_pages', '0008_remove_gallerypagegalleryimage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerypagegalleryimage',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
