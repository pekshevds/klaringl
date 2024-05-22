from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator
from index_app.forms import GetInTouchForm
from index_app.models import (
    News,
    Vacancy
)


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        news = News.last_news.all()
        context = {
            "news": news
        }
        return render(request,
                      "index_app/index.html",
                      context)


class AboutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/about/index.html",
                      {})


class NewsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        item_list = News.active_news.all()
        paginator = Paginator(item_list, 9)
        page_number = request.GET.get("page", 1)
        items = paginator.get_page(page_number)
        context = {
            "items": items,
            "iterator": [i for i in range(1, items.paginator.num_pages + 1)]
        }
        return render(request,
                      "index_app/about/news_list.html",
                      context)


class NewsView(View):
    def get(self, request: HttpRequest, id: str) -> HttpResponse:
        item = News.objects.get(id=id)
        context = {
            "item": item
        }
        return render(request,
                      "index_app/about/news.html",
                      context)


class VacancyListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        item_list = Vacancy.active_vacancies.all()
        paginator = Paginator(item_list, 9)
        page_number = request.GET.get("page", 1)
        items = paginator.get_page(page_number)
        context = {
            "items": items,
            "iterator": [i for i in range(1, items.paginator.num_pages + 1)]
        }
        return render(request,
                      "index_app/about/vacancy_list.html",
                      context)


class VacancyView(View):
    def get(self, request: HttpRequest, id: str) -> HttpResponse:
        item = Vacancy.objects.get(id=id)
        context = {
            "item": item
        }
        return render(request,
                      "index_app/about/vacancy.html",
                      context)


class CooperationView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/about/cooperation.html",
                      {})


class BlogView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/about/blog/index.html",
                      {})


class DocumentationView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/documentation.html",
                      {})


class ContactsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/contacts.html",
                      {})


class BranchOfficesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/branch_offices.html",
                      {})


class ServicesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/services/index.html",
                      {})


class DeliveryOfGroupageCargoView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/services/delivery_of_groupage_cargo.html",
                      {})


class AdditionalServicesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/services/additional_services.html",
                      {})


class CompleteSolutionsForBusinessView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/services/complete_solutions_for_business.html",
                      {})


class SolutionsForOnlineStoresView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/services/solutions_for_online_stores.html",
                      {})


class PrivacyPolicyView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/privacypolicy.html",
                      {})


class GetInTouchView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return redirect("index:contacts")
