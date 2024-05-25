from django.urls import path
from calculator_app.views import (
    CityView,
    RateView,
    CalculateView
)


app_name = 'calculator_app'

urlpatterns = [
    path('cities/', CityView.as_view(), name="city"),
    path('rates/', RateView.as_view(), name="rate"),
    path('calculate/', CalculateView.as_view(), name="calculate"),
]
