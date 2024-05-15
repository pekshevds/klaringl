from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import View
from index_app.forms import GetInTouchForm


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/index.html",
                      {})


class AboutUsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/aboutus.html",
                      {})


class AboutOurCompanyView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/aboutourcompany.html",
                      {})


class NewsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/news.html",
                      {})


class FeedbackView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/feedback.html",
                      {})


class ContactView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/contact.html",
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
        return redirect("index:contact")
