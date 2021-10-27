from django.db import models

# Create your models here.
class Map(models.Model):
    lat_1 = models.FloatField(default=1.0)
    long_1 = models.FloatField(default=1.0)
    
class Age(models.Model):
    age_id = models.IntegerField(default=0)
    perc0_5 = models.FloatField(default=0)
    perc5_9 = models.FloatField(default=0)
    perc10_14 = models.FloatField(default=0)
    perc15_17 = models.FloatField(default=0)
    perc18_24 = models.FloatField(default=0)
    perc25_34 = models.FloatField(default=0)
    perc35_44 = models.FloatField(default=0)
    perc45_54 = models.FloatField(default=0)
    perc55_64 = models.FloatField(default=0)
    perc65_74 = models.FloatField(default=0)
    perc75_84 = models.FloatField(default=0)
    perc85UP = models.FloatField(default=0)

    COVID_CASES = '1'
    MEDIAN_INCOME = '2'
    INSURANCE_COVERAGE = '3'
    MAP_CHOICES = [
        (COVID_CASES, 'Covid_Cases'),
        (MEDIAN_INCOME, 'Median_Income'),
        (INSURANCE_COVERAGE, 'Insurance_Coverage'),
    ]
    map_choice = models.CharField(
        max_length = 1,
        choices = MAP_CHOICES,
        default = COVID_CASES,
    )


    #Run a select query to get database views in the init file to join the 3 tables (Data/County/Latlong) & Then Populate Map using those..
    #

    
