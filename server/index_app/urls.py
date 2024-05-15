from django.urls import path
from index_app.views import (
    IndexView,
    AboutUsView,
    ContactView,
    AboutOurCompanyView,
    FeedbackView,
    NewsView,
    GetInTouchView,
    PrivacyPolicyView
)

app_name = "index"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about-us/', AboutUsView.as_view(), name="about-us"),
    path('about-our-company/', AboutOurCompanyView.as_view(), name="about-our-company"),
    path('contacts/', ContactView.as_view(), name="contacts"),
    path('get-in-touch/', GetInTouchView.as_view(), name="get-in-touch"),
    path('feedback/', FeedbackView.as_view(), name="feedback"),
    path('news/', NewsView.as_view(), name="news"),
    path('privacy/', PrivacyPolicyView.as_view(), name="privacy"),
]
