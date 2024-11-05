from django.urls import path
from .views import CalcView, CheckView

app_name = "calculator"

urlpatterns = [
    path("", CalcView.as_view(), name="calc"),
    path("check/", CheckView.as_view(), name="check"),
]
