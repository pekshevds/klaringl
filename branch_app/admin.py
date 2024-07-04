from django.contrib import admin
from branch_app.models import Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at",
                    "address", "email", "tel", "active"]
    search_fields = ["name", "address"]
