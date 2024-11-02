from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib.auth import logout

from datetime import datetime, timedelta

from index_app.forms import GetInTouchForm, MessageForm
from index_app.models import News, Vacancy, Document, Const, Branch, Question
from calculator_app.models import Rate
from order_app.services import fetch_customer_orders


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        news = News.last_news.all()
        context = {
            "const": Const.info(),
            "cities_list": Rate.cities_to,
            "cities_from_list": Rate.cities_from,
            "news": news,
            "title": "Решения для логистики, перевозок и доставки.",
        }
        return render(request, "index_app/index.html", context)


class AboutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info()}
        return render(request, "index_app/about/index.html", context)


class NewsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        item_list = News.active_news.all()
        paginator = Paginator(item_list, 9)
        page_number = request.GET.get("page", 1)
        items = paginator.get_page(page_number)
        context = {
            "const": Const.info(),
            "items": items,
            "iterator": [i for i in range(1, items.paginator.num_pages + 1)],
        }
        return render(request, "index_app/about/news_list.html", context)


class NewsView(View):
    def get(self, request: HttpRequest, id: str) -> HttpResponse:
        item = News.objects.get(id=id)
        context = {"const": Const.info(), "item": item}
        return render(request, "index_app/about/news.html", context)


class VacancyListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        item_list = Vacancy.active_vacancies.all()
        paginator = Paginator(item_list, 9)
        page_number = request.GET.get("page", 1)
        items = paginator.get_page(page_number)
        context = {
            "const": Const.info(),
            "items": items,
            "iterator": [i for i in range(1, items.paginator.num_pages + 1)],
        }
        return render(request, "index_app/about/vacancy_list.html", context)


class VacancyView(View):
    def get(self, request: HttpRequest, id: str) -> HttpResponse:
        item = Vacancy.objects.get(id=id)
        context = {"const": Const.info(), "item": item}
        return render(request, "index_app/about/vacancy.html", context)


class CooperationView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info()}
        return render(request, "index_app/about/cooperation.html", context)


class BlogView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info()}
        return render(request, "index_app/about/blog/index.html", context)


class DocumentationView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        items = Document.active_documents.all()
        context = {"const": Const.info(), "items": items}
        return render(request, "index_app/documentation.html", context)


class BranchOfficesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info(), "items": Branch.active_branchs.all()}
        return render(request, "index_app/branches.html", context)


class ContactsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info(), "questions": Question.objects.all()}
        return render(request, "index_app/contacts.html", context)


class ServicesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info()}
        return render(request, "index_app/services/index.html", context)


class DeliveryOfGroupageCargoView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info()}
        return render(
            request, "index_app/services/delivery_of_groupage_cargo.html", context
        )


class AdditionalServicesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info()}
        return render(request, "index_app/services/additional_services.html", context)


class CompleteSolutionsForBusinessView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info()}
        return render(
            request, "index_app/services/complete_solutions_for_business.html", context
        )


class SolutionsForOnlineStoresView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info()}
        return render(
            request, "index_app/services/solutions_for_online_stores.html", context
        )


class PrivacyPolicyView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info()}
        return render(request, "index_app/privacypolicy.html", context)


class GetInTouchView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return redirect("index:contacts")


class MessageView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        form = MessageForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return redirect(request.META.get("HTTP_REFERER"))


class LkView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            context = {"const": Const.info()}
            date_from = request.GET.get(
                "date_from",
                (datetime.now() - timedelta(days=4)).date().strftime("%Y-%m-%d"),
            )
            date_to = request.GET.get(
                "date_to", datetime.now().date().strftime("%Y-%m-%d")
            )
            context.update({"date_from": date_from, "date_to": date_to})
            id = request.user.customer.id
            result = fetch_customer_orders(
                customer_id=id, date_from=date_from, date_to=date_to
            )
            total_volume = 0
            total_weight = 0
            summ = 0
            if result:
                orders_list = result.get("orders", [])
                for item in orders_list:
                    summ += item.get("summ", 0)
                    total_volume += item.get("volume", 0)
                    total_weight += item.get("weight", 0)
                totals = {
                    "summ": format(summ, ".2f"),
                    "total_volume": format(total_volume, ".2f"),
                    "total_weight": format(total_weight, ".2f"),
                }
                context.update(
                    {
                        "orders_list": orders_list,
                        "order_totals": totals,
                    }
                )
            return render(request, "index_app/lk.html", context)
        else:
            return redirect("index:login")


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("index:lk")
        else:
            context = {"const": Const.info()}
            return render(request, "index_app/login.html", context)


class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"const": Const.info()}
        if request.user.is_authenticated:
            logout(request)
        return redirect("index:login")
