from django.urls import path
from index_app.views import (
    IndexView,
    AboutView,
    NewsListView,
    NewsView,
    VacancyListView,
    VacancyView,
    CooperationView,
    BlogView,
    ServicesView,
    DeliveryOfGroupageCargoView,
    AdditionalServicesView,
    CompleteSolutionsForBusinessView,
    SolutionsForOnlineStoresView,
    DocumentationView,
    ContactsView,
    MessageView
)

app_name = "index"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("about/news/", NewsListView.as_view(), name="news"),
    path("about/news/<str:id>", NewsView.as_view(), name="open-news"),
    path("about/vacancies/", VacancyListView.as_view(), name="vacancies"),
    path("about/vacancies/<str:id>", VacancyView.as_view(), name="open-vacancy"),
    path("about/cooperation/", CooperationView.as_view(), name="cooperation"),
    path("about/blog/", BlogView.as_view(), name="blog"),

    path("services/", ServicesView.as_view(), name="services"),
    path("services/delivery_of_groupage_cargo/",
         DeliveryOfGroupageCargoView.as_view(),
         name="delivery-of-groupage-cargo"),
    path("services/additional_services/",
         AdditionalServicesView.as_view(),
         name="additional-services"),
    path("services/complete_solutions_for_business/",
         CompleteSolutionsForBusinessView.as_view(),
         name="complete-solutions-for-business"),
    path("services/solutions_for_online_stores/",
         SolutionsForOnlineStoresView.as_view(),
         name="solutions-for-online-stores"),
    path("documentation/", DocumentationView.as_view(), name="documentation"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("message/", MessageView.as_view(), name="message"),
]
