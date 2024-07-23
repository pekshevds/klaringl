import logging
import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication

# from server.base import FormOfOwnershipSelector, PayerSelector
from order_app.models import Cargo, Order
from order_app.serializers import (
    CargorSerializer,
    OrderSerializer,
    MakrUploadedSerializer,
)
from calculator_app.models import Rate
from order_app.services import fetch_order_status_by_number

logger = logging.getLogger(__name__)


class CargoAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Cargo.objects.all()
        serializer = CargorSerializer(queryset, many=True)
        response = {"data": serializer.data, "count": len(queryset), "success": True}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [], "count": 0, "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        logger.info(json.dumps(data))
        serializer = CargorSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            response["count"] = len(serializer.data)
            response["success"] = True
        return Response(response)


class NotUploadedOrderAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Order.objects.filter(uploaded=False)
        serializer = OrderSerializer(queryset, many=True)
        response = {"data": serializer.data, "count": len(queryset), "success": True}
        return Response(response)


class OrderAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        response = {"data": serializer.data, "count": len(queryset), "success": True}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [], "count": 0, "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        logger.info(json.dumps(data))
        serializer = OrderSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            response["count"] = len(serializer.data)
            response["success"] = True
        return Response(response)


class CheckStatusAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        response = {"data": [], "count": 0, "success": False}
        num = request.GET.get("num")
        if not num:
            return Response(response)
        response["data"] = [{"status": fetch_order_status_by_number(order_number=num)}]
        response["count"] = 1
        response["success"] = True
        return Response(response)


# class NewOrderView(View):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.AllowAny]

#     def get(self, request: HttpRequest) -> HttpResponse:
#         context = {
#             "cities_list": Rate.cities_to,
#             "cities_from_list": Rate.cities_from,
#             "payer_selector": dict(PayerSelector.choices),
#             "form_ownership_selector": dict(FormOfOwnershipSelector.choices),
#         }
#         return render(request, "order_app/new-order.html", context)


class MarkUploadedAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> HttpResponse:
        response = {"data": [], "count": 0, "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        serializer = MakrUploadedSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        response["success"] = True
        return Response(response)
