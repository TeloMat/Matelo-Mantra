# Generated by Django 3.1.7 on 2021-05-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_picturealbum_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='photo',
            field=models.ImageField(blank=True, upload_to='travels/pictures'),
        ),
        migrations.AlterField(
            model_name='picturealbum',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='travels/thumbnails'),
        ),
    ]