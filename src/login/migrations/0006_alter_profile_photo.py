# Generated by Django 3.2.9 on 2021-12-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20211208_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='cat.jpeg', upload_to='login/MEDIA/profile/photos'),
        ),
    ]
