# Generated by Django 3.2.7 on 2021-11-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0010_health_stats_labor_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_stats',
            name='percent_insured',
            field=models.FloatField(default=0),
        ),
    ]
