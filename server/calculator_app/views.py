from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import View


class CalcView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      "calculator_app/calc.html",
                      {})
