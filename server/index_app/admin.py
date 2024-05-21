from django.contrib import admin
from index_app.models import (
    News,
    Vacancy
)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at", "active"]
    search_fields = ["name"]
    list_filter = ["active"]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["name", "salary", "created_at", "updated_at", "active"]
    search_fields = ["name"]
    list_filter = ["active"]
