from django.urls import path
from index_app.views import IndexView

app_name = "index"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]
