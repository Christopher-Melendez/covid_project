from django.db import models

# Create your models here.
class covid_cases(models.Model):
    id = models.BigIntegerField(primary_key='true', default=0)
    test_date = models.CharField(default=0, max_length=100)
    county = models.CharField(default=0, max_length=100)
    new_positives = models.IntegerField(default=0)
    Cumulative_num_posi = models.IntegerField(default=0)
    total_tests_day = models.IntegerField(default=0)
    cumul_tests = models.IntegerField(default=0)
    C_Pos_C_Test = models.FloatField(default=0)

class covid_deaths(models.Model):
    id = models.BigIntegerField(primary_key='true', default=0)
    report_date = models.CharField(default=0, max_length=100)
    county = models.CharField(default=0, max_length=100)
    total_deaths = models.IntegerField(default=0)
    population = models.IntegerField(default=0)
    deaths_percent = models.FloatField(default=0)
    deaths_per100 = models.FloatField(default=0)

class labor_stats(models.Model):
  id = models.BigIntegerField(primary_key="True", default=0)
  county = models.CharField(default=0, max_length=100)
  median_income = models.IntegerField(default=0)
  percent_college = models.FloatField(default=0)
  percent_unemployed = models.FloatField(default=0)
  percent_poverty = models.FloatField(default=0)

class health_stats(models.Model):
   id = models.BigIntegerField(primary_key="True", default=0)
   county = models.CharField(default=0, max_length=100)
   percent_insured = models.FloatField(default=0)
