from django.urls import path
from rest_framework.authtoken import views
from calculator_app.views import (
    CityAPIView,
    CityFromAPIView,
    CityToAPIView,
    RateAPIView,
    ExpeditionRateAPIView,
    FastCalculateAPIView,
    CalculateAPIView,
)
from order_app.views import (
    CargoAPIView,
    OrderAPIView,
    CheckStatusAPIView,
    MarkUploadedAPIView,
    NotUploadedOrderAPIView,
)
from api_app.views import CheckConnectionAPIView


app_name = "api"

urlpatterns = [
    path("calculator/cities/", CityAPIView.as_view(), name="city"),
    path("calculator/cities/from/", CityFromAPIView.as_view(), name="city-from"),
    path("calculator/cities/to/", CityToAPIView.as_view(), name="city-to"),
    path("calculator/rates/", RateAPIView.as_view(), name="rate"),
    path(
        "calculator/expedition-rates/",
        ExpeditionRateAPIView.as_view(),
        name="expedition-rate",
    ),
    path(
        "calculator/fast-calculate/",
        FastCalculateAPIView.as_view(),
        name="fast-calculate",
    ),
    path("calculator/calculate/", CalculateAPIView.as_view(), name="calculate"),
    path("order/cargos/", CargoAPIView.as_view(), name="cargo"),
    path("order/orders/", OrderAPIView.as_view(), name="order"),
    path("order/check-status/", CheckStatusAPIView.as_view(), name="check-status"),
    path("order/mark-order/", MarkUploadedAPIView.as_view(), name="mark-order"),
    path("order/new-orders/", NotUploadedOrderAPIView.as_view(), name="new-orders"),
    path("api-token-auth/", views.obtain_auth_token),
    path(
        "check-connection/", CheckConnectionAPIView.as_view(), name="check-connection"
    ),
]
