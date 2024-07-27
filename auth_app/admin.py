from django.contrib import admin
from auth_app.models import User, Pin, Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ["id", "name"]
    list_display = ["name"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "customer"]


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ["pin_code", "used", "user"]
    list_filter = ["user"]
    raw_id_fields = ["user"]
    date_hierarchy = "use_before"
    ordering = ["used", "use_before"]
