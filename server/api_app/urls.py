from django.urls import path, include
from rest_framework.authtoken import views


app_name = 'api_app'

urlpatterns = [
    path('calculator/',
         include('calculator_app.urls', namespace='calculator_app')),
    path('api-token-auth/', views.obtain_auth_token),
]
