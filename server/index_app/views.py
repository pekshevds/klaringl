from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import View
from index_app.forms import GetInTouchForm


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/index.html",
                      {})


class AboutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/about/index.html",
                      {})


class NewsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/about/news.html",
                      {})


class VacanciesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/about/vacancies.html",
                      {})


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
