import logging
import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication

from server.base import FormOfOwnershipSelector, PayerSelector
from calculator_app.models import City, Rate
from calculator_app.serializers import (
    CitySerializer,
    RateSerializer,
    FastCalculateRequestSerializer,
    CalculateRequestSerializer,
    CalculateResponseSerializer,
)
from calculator_app.services import calculate_delivery_cost, calculate_order
import config

logger = logging.getLogger(__name__)


class CityFromAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Rate.cities_from.all()
        serializer = CitySerializer(queryset, many=True)
        response = {"data": serializer.data, "count": len(queryset), "success": True}
        return Response(response)


class CityToAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Rate.cities_to.all()
        serializer = CitySerializer(queryset, many=True)
        response = {"data": serializer.data, "count": len(queryset), "success": True}
        return Response(response)


class CityAPIView(APIView):
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.BasicAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        response = {"data": serializer.data, "count": len(queryset), "success": True}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [], "count": 0, "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        serializer = CitySerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            response["count"] = len(serializer.data)
            response["success"] = True
        return Response(response)


class RateAPIView(APIView):
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.BasicAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Rate.objects.all()
        serializer = RateSerializer(queryset, many=True)
        response = {"data": serializer.data, "count": len(queryset), "success": True}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [], "count": 0, "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        serializer = RateSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            response["count"] = len(serializer.data)
            response["success"] = True
        return Response(response)


class CalculateAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        response = {"data": {}, "count": 0, "success": False}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        logger.info(data)
        serializer = CalculateRequestSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # cost = calculate_delivery_cost(**serializer.validated_data)
            cost = calculate_order(serializer.validated_data)
            serializer = CalculateResponseSerializer({"cost": cost})
            response = {"data": serializer.data, "count": 1, "success": True}
        return Response(response)


class FastCalculateAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        response = {"data": {}, "count": 0, "success": False}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        logger.info(data)
        serializer = FastCalculateRequestSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            cost = calculate_delivery_cost(**serializer.validated_data)
            serializer = CalculateResponseSerializer({"cost": cost})
            response = {"data": serializer.data, "count": 1, "success": True}
        return Response(response)


# процедура вывода страницы Калькулятор стоимости перевозки
def createChoisesJson(choises) -> dict:
    choises_list = []
    for key, value in choises:
        choises_list.append({
            "value": key,
            "label": value
        }) 
    return choises_list
def createCitiesJson(query_cities_list) -> dict:
    dict_cities_list = []
    for item in query_cities_list:
        id = "{}".format(item.pk).replace('\ufeff', '')
        name = "{}".format(item.name).replace('\ufeff', '')
        dict_cities_list.append({
            "value": id,
            "label": name
        }) 
    return dict_cities_list

class CalcView(View):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "cities_list": json.dumps(createCitiesJson(Rate.cities_to())),
            "cities_from_list": json.dumps(createCitiesJson(Rate.cities_from())),
            "payer_selector": json.dumps(createChoisesJson(PayerSelector.choices)),
            "form_ownership_selector": json.dumps(createChoisesJson(FormOfOwnershipSelector.choices)),
        }
        city_from_id = request.GET.get('city_from_id')
        if city_from_id:
            context.update({
                "city_from_id": city_from_id
            })
        city_to_id = request.GET.get('city_to_id')
        if city_to_id:
            context.update({
                "city_to_id": city_to_id
            })
        weight = request.GET.get('weight')
        if weight:
            context.update({
                "weight": weight
            }) 
        volume = request.GET.get('volume')
        if volume:
            context.update({
                "volume": volume
            })
        return render(request, "calculator_app/calc.html", context)
