from django.shortcuts import render
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
                      "index_app/about.html",
                      {})


class ContactView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "index_app/contact.html",
                      {})


class GetInTouchView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request,
                      "index_app/contact.html",
                      {})
