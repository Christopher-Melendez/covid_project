# Generated by Django 3.2.7 on 2021-12-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0012_merge_20211130_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_stats',
            name='percent_insured',
            field=models.FloatField(default=0),
        ),
    ]
