# Generated by Django 3.2.7 on 2021-11-03 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_alter_covid_cases_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('age_id', models.IntegerField(default=0, primary_key='True', serialize=False)),
                ('perc0_5', models.FloatField(default=0)),
                ('perc5_9', models.FloatField(default=0)),
                ('perc10_14', models.FloatField(default=0)),
                ('perc15_17', models.FloatField(default=0)),
                ('perc18_24', models.FloatField(default=0)),
                ('perc25_34', models.FloatField(default=0)),
                ('perc35_44', models.FloatField(default=0)),
                ('perc45_54', models.FloatField(default=0)),
                ('perc55_64', models.FloatField(default=0)),
                ('perc65_74', models.FloatField(default=0)),
                ('perc75_84', models.FloatField(default=0)),
                ('perc85UP', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ethnicity_id',
            fields=[
                ('ethnicity_id', models.IntegerField(default=0, primary_key='True', serialize=False)),
                ('perc_white', models.FloatField(default=0)),
                ('perc_african_american', models.FloatField(default=0)),
                ('perc_native_american', models.FloatField(default=0)),
                ('perc_asian', models.FloatField(default=0)),
                ('perc_pacific_islander', models.FloatField(default=0)),
                ('perc_other', models.FloatField(default=0)),
                ('perc_two_or_more', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='income_id',
            fields=[
                ('c_income_id', models.FloatField(default=0.0, primary_key='true', serialize=False)),
                ('perc_0_10', models.FloatField(default=0.0)),
                ('perc_10_15', models.FloatField(default=0.0)),
                ('perc_15_20', models.FloatField(default=0.0)),
                ('perc_20_25', models.FloatField(default=0.0)),
                ('perc_25_30', models.FloatField(default=0.0)),
                ('perc_30_35', models.FloatField(default=0.0)),
                ('perc_35_40', models.FloatField(default=0.0)),
                ('perc_40_45', models.FloatField(default=0.0)),
                ('perc_45_50', models.FloatField(default=0.0)),
                ('perc_50_60', models.FloatField(default=0.0)),
                ('perc_60_75', models.FloatField(default=0.0)),
                ('perc_75_100', models.FloatField(default=0.0)),
                ('perc_100_125', models.FloatField(default=0.0)),
                ('perc_125_150', models.FloatField(default=0.0)),
                ('perc_150_200', models.FloatField(default=0.0)),
                ('perc_200_up', models.FloatField(default=0.0)),
                ('med_income', models.FloatField(default=0.0)),
            ],
        ),
    ]