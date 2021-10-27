from django.db import models

# Create your models here.
class Map(models.Model):
    lat_1 = models.FloatField(default=1.0)
    long_1 = models.FloatField(default=1.0)

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
class income_id(models,Model):
    c_income_id = models.FloadField(default=0.0)
    perc_0-10 = models.FloatField(default=0.0)
    perc_10-15 = models.FloatField(default=0.0)
    perc_15-20 = models.FloatField(default=0.0)
    perc_20-25 =  models.FloatField(default=0.0)
    perc_25-30 =  models.FloatField(default=0.0)
    perc_30-35 =  models.FloatField(default=0.0)
    perc_35-40 =  models.FloatField(default=0.0)
    perc_40-45 =  models.FloatField(default=0.0)
    perc_45-50 =  models.FloatField(default=0.0)
    perc_50-60 =  models.FloatField(default=0.0)
    perc_60-75 =  models.FloatField(default=0.0)
    perc_75-100 =  models.FloatField(default=0.0)
    perc_100-125 =  models.FloatField(default=0.0)
    perc_125-150 =  models.FloatField(default=0.0)
    perc_150-200 =  models.FloatField(default=0.0)
    perc_200-up =  models.FloatField(default=0.0)
    med_income =  models.FloatField(default=0.0)

    
    

    #Run a select query to get database views in the init file to join the 3 tables (Data/County/Latlong) & Then Populate Map using those..
    #

    
class ethnicity_id(models.Model):
    ethnicity_id = models.FloatField(default=0)
    perc_white = models.FloatField(default=0)
    perc_african_american = models.FloatField(default=0)
    perc_native_american = models.FloatField(default=0)
    perc_asian = models.FloatField(default=0)
    perc_pacific_islander= models.FloatField(default=0)
    perc_other = models.FloatField(default=0)
    perc_two_or_more = models.FloatField(default=0)


class covid_cases(models.Model):
    test_date = models.CharField(default=0)
    county = models.CharField(default=0)
    new_positives = models.FloatField(default=0)
    Cumulative_num_posi = models.FloatField(default=0)
    total_tests_day = models.FloatField(default=0)
    cumul_tests = models.FloatField(default=0)
    C_Pos_C_Test = models.FloatField(default=0)

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