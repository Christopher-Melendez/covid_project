# Generated by Django 3.2.9 on 2021-12-08 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20211206_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default=0, upload_to='profile/photos'),
        ),
    ]
