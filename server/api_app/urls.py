from django.urls import path
from rest_framework.authtoken import views
from calculator_app.views import (
    CityAPIView,
    RateAPIView,
    CalculateAPIView
)
from order_app.views import (
    CargoAPIView
)


app_name = 'api_app'

urlpatterns = [
    path('calculator/cities/', CityAPIView.as_view(), name="city"),
    path('calculator/rates/', RateAPIView.as_view(), name="rate"),
    path('calculator/calculate/', CalculateAPIView.as_view(), name="calculate"),
    path('order/cargos/', CargoAPIView.as_view(), name="cargo"),
    path('api-token-auth/', views.obtain_auth_token),
]
