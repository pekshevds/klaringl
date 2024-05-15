from django.contrib import admin
from order_app.models import (
    City,
    Rate
)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ["__str__",
                    "cost_by_weight_0_25", "cost_by_weight_25_50",
                    "cost_by_weight_50_150", "cost_by_weight_150_300",
                    "cost_by_weight_300_500", "cost_by_weight_500_1000",
                    "cost_by_weight_1000_1500", "cost_by_weight_1500_2000",
                    "cost_by_weight_2000_3000", "cost_by_weight_3000_5000",
                    "cost_by_weight_5000_10000", "cost_by_weight_10000_inf"
                    ]
