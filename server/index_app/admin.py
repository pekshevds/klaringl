from django.contrib import admin
from index_app.models import (
    News,
    Vacancy,
    Document,
    Tag,
    Const
)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at",
                    "active", "author", "tag"]
    search_fields = ["name"]
    list_filter = ["active", "author", "tag"]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["name", "salary", "created_at", "updated_at", "active"]
    search_fields = ["name"]
    list_filter = ["active"]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at", "active"]
    search_fields = ["name"]
    list_filter = ["active"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]


@admin.register(Const)
class ConstAdmin(admin.ModelAdmin):
    list_display = ["address", "tel", "email", "created_at", "updated_at"]
    search_fields = ["address"]
