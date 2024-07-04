from django.urls import path
from branch_app.views import (
    BranchOfficesView
)

app_name = "branch"

urlpatterns = [
    path("", BranchOfficesView.as_view(), name="branch-offices"),
]
