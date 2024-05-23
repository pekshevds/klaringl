from django.urls import path
from .views import (
    CalcView
)

urlpatterns = [
    path('', CalcView.as_view(), name="calc"),
]