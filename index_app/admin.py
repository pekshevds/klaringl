from django.contrib import admin
from index_app.models import News, Vacancy, Document, Tag, Branch, Const, Question

admin.site.site_header = "Панель администрирования klaringl"
admin.site.site_title = "Панель администрирования klaringl"
admin.site.index_title = "Добро пожаловать!"


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
    list_display = ["address", "tel", "email", "created_at", "updated_at"]
    search_fields = ["address"]
