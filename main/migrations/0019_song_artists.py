# Generated by Django 3.2.4 on 2021-06-15 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210508_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artists',
            field=models.CharField(default='Matelo Mantra', max_length=100),
        ),
    ]
