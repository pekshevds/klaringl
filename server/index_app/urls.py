from django.urls import path
from index_app.views import (
    IndexView,
    AboutView,
    ContactView
)

app_name = "index"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
]
