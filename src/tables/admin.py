from django.contrib import admin

# Register your models here.

from .models import covid_cases
admin.site.register(covid_cases)

from .models import covid_deaths
admin.site.register(covid_deaths)

from .models import labor_stats
admin.site.register(labor_stats)

from .models import health_stats
admin.site.register(health_stats)

