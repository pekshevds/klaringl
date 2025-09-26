from django.utils.html import format_html
from django.contrib import admin
from index_app.models import (
    News,
    Vacancy,
    Document,
    Tag,
    Branch,
    Const,
    Question,
    Picture,
)

admin.site.site_header = "Панель администрирования klaringl"
admin.site.site_title = "Панель администрирования klaringl"
admin.site.index_title = "Добро пожаловать!"


def _preview(obj: Picture, attr_name: str):
    season = getattr(obj, attr_name)
    if not season:
        return ""
    if not season.image:
        return ""
    str = f"'<img src={season.image.url} style='max-height: 75px;'>"
    return format_html(str)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
        "updated_at",
        "preview",
    )
    search_fields = [
        "name",
    ]

    def preview(self, obj: Picture) -> str:
        if obj.image:
            str = f"'<img src={obj.image.url} style='max-height: 75px;'>"
            return format_html(str)
        return ""

    setattr(preview, "short_description", "Изображение")


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "created_at",
        "updated_at",
        "address",
        "email",
        "tel",
        "active",
    ]
    search_fields = ["name", "address"]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at", "active", "author", "tag"]
    search_fields = ["name"]
    list_filter = ["active", "author", "tag"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]


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
    list_display = [
        "address",
        "tel",
        "email",
        "created_at",
        "updated_at",
        "preview_autumn",
        "preview_spring",
        "preview_summer",
        "preview_winter",
    ]
    search_fields = ["address"]

    def preview_autumn(self, obj: Picture) -> str:
        return _preview(obj, "autumn")

    def preview_spring(self, obj: Picture) -> str:
        return _preview(obj, "spring")

    def preview_summer(self, obj: Picture) -> str:
        return _preview(obj, "summer")

    def preview_winter(self, obj: Picture) -> str:
        return _preview(obj, "winter")

    setattr(preview_autumn, "short_description", "Осень")
    setattr(preview_spring, "short_description", "Весна")
    setattr(preview_summer, "short_description", "Лето")
    setattr(preview_winter, "short_description", "Зима")
