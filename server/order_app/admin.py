from django.contrib import admin
from order_app.models import (
    Cargo,
    Order,
    ItemOrder
)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "weight",
                    "length", "width", "height",
                    "volume"]
    search_fields = ["id"]


class ItemOrderInLine(admin.TabularInline):
    model = ItemOrder
    raw_id_fields = ["cargo"]
    # prepopulated_fields = {"name": ["name"]}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemOrderInLine]
    list_display = ["__str__", "city_from", "date_from",
                    "city_to", "date_to", "declared_cost", "cost"]
    list_filter = ["city_from"]
    search_fields = ["number"]
    date_hierarchy = "date"
    readonly_fields = ("cost",)


"""@admin.register(ItemOrder)
class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ["order", "id", "cargo"]
    search_fields = ["order_number"]"""
