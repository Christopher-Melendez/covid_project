# Generated by Django 3.2.8 on 2021-11-10 05:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_alter_profile_last_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_active',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 10, 5, 26, 19, 781073)),
        ),
    ]
