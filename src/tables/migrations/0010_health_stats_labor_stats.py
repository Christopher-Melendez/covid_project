# Generated by Django 3.2.7 on 2021-11-29 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0009_auto_20211129_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='health_stats',
            fields=[
                ('id', models.BigIntegerField(default=0, primary_key='True', serialize=False)),
                ('county', models.CharField(default=0, max_length=100)),
                ('percent_insured', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='labor_stats',
            fields=[
                ('id', models.BigIntegerField(default=0, primary_key='True', serialize=False)),
                ('county', models.CharField(default=0, max_length=100)),
                ('median_income', models.IntegerField(default=0)),
                ('percent_college', models.FloatField(default=0)),
                ('percent_unemployed', models.FloatField(default=0)),
                ('percent_poverty', models.FloatField(default=0)),
            ],
        ),
    ]