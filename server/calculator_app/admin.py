from django.contrib import admin
from calculator_app.models import (
    City,
    Rate,
    RateItem,
    LastMileRate
)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(RateItem)
class RateItemAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    fieldsets = [
        ("Города", {
            "fields": ["city_from", "city_to"]
        }),
        ("Прайс ПО ВЕСУ (цена в рублях за 1 кг)", {
            "fields": ["cost_by_weight_0_25", "cost_by_weight_25_50",
                       "cost_by_weight_50_150", "cost_by_weight_150_300",
                       "cost_by_weight_300_500", "cost_by_weight_500_1000",
                       "cost_by_weight_1000_1500", "cost_by_weight_1500_2000",
                       "cost_by_weight_2000_3000", "cost_by_weight_3000_5000",
                       "cost_by_weight_5000_10000", "cost_by_weight_10000_inf"]
        },),
        ("Прайс ПО ОБЪЕМУ (цена в рублях за 1 м3)", {
            "fields": ["cost_by_volume_0_01", "cost_by_volume_01_02",
                       "cost_by_volume_02_06", "cost_by_volume_06_12",
                       "cost_by_volume_12_20", "cost_by_volume_20_40",
                       "cost_by_volume_40_60", "cost_by_volume_60_80",
                       "cost_by_volume_80_120", "cost_by_volume_120_200",
                       "cost_by_volume_200_400", "cost_by_volume_400_inf"]
        },),
    ]
    list_filter = ["city_from", "city_to"]


@admin.register(LastMileRate)
class LastMileRateAdmin(admin.ModelAdmin):
    list_display = ["rate_item"]
    fieldsets = [
        ("Города", {
            "fields": ["rate_item"]
        }),
        ("Прайс ПО ВЕСУ (цена в рублях за 1 кг)", {
            "fields": ["cost_by_weight_0_25", "cost_by_weight_25_50",
                       "cost_by_weight_50_150", "cost_by_weight_150_300",
                       "cost_by_weight_300_500", "cost_by_weight_500_1000",
                       "cost_by_weight_1000_1500", "cost_by_weight_1500_2000",
                       "cost_by_weight_2000_3000", "cost_by_weight_3000_5000",
                       "cost_by_weight_5000_10000",
                       "cost_by_weight_10000_20000",
                       "cost_by_weight_20000_inf"]
        },),
        ("Прайс ПО ОБЪЕМУ (цена в рублях за 1 м3)", {
            "fields": ["cost_by_volume_0_01", "cost_by_volume_01_02",
                       "cost_by_volume_02_06", "cost_by_volume_06_12",
                       "cost_by_volume_12_20", "cost_by_volume_20_40",
                       "cost_by_volume_40_60", "cost_by_volume_60_80",
                       "cost_by_volume_80_120", "cost_by_volume_120_200",
                       "cost_by_volume_200_400", "cost_by_volume_400_800",
                       "cost_by_volume_800_inf"]
        },),
    ]
    list_filter = ["rate_item"]
