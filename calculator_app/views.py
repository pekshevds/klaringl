from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (
    permissions,
    authentication
)

from calculator_app.models import (
    City,
    Rate
)
from calculator_app.serializers import (
    CitySerializer,
    RateSerializer,
    FastCalculateRequestSerializer,
    CalculateRequestSerializer,
    CalculateResponseSerializer
)
from calculator_app.services import (
    calculate_delivery_cost,
    calculate_order
)
import config


class CityFromAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Rate.cities_from.all()
        serializer = CitySerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)


class CityToAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Rate.cities_to.all()
        serializer = CitySerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)


class CityAPIView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [],
                    "count": 0,
                    "success": False}
        data = request.data.get("data", None)
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

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Rate.objects.all()
        serializer = RateSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)


class CalculateAPIView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request: HttpRequest) -> HttpResponse:
        response = {"data": {},
                    "count": 0,
                    "success": False}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        serializer = CalculateRequestSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # cost = calculate_delivery_cost(**serializer.validated_data)
            cost = calculate_order(serializer.validated_data)
            serializer = CalculateResponseSerializer({"cost": cost})
            response = {"data": serializer.data,
                        "count": 1,
                        "success": True}
        return Response(response)


class FastCalculateAPIView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        response = {"data": {},
                    "count": 0,
                    "success": False}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        serializer = FastCalculateRequestSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            cost = calculate_delivery_cost(**serializer.validated_data)
            serializer = CalculateResponseSerializer({"cost": cost})
            response = {"data": serializer.data,
                        "count": 1,
                        "success": True}
        return Response(response)


# процедура вывода страницы Калькулятор стоимости перевозки


class CalcView(View):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        server_api_token = config.SERVER_API_TOKEN
        context = {
            "cities_list": Rate.cities_to,
            "cities_from_list":  Rate.cities_from,
            "server_api_token": server_api_token
        }
        return render(request,
                      "calculator_app/calc.html",
                      context)
