# Generated by Django 3.2.7 on 2021-11-03 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_auto_20211102_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid_cases',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
