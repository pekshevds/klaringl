from django.urls import path
from .views import NewOrderView

app_name = "order"

urlpatterns = [
    path("new-order/", NewOrderView.as_view(), name="new-order"),
]
