from django.urls import path
from .views import (
    CalcView
)

app_name = 'calculator_app'

urlpatterns = [
    path('', CalcView.as_view(), name="calc"),
]
