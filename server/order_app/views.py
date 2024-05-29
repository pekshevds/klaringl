from django.http import HttpRequest, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (
    permissions,
    authentication
)
from order_app.models import (
    Cargo,
    Order
)
from order_app.serializers import (
    CargorSerializer,
    OrderSerializer
)


class CargoAPIView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Cargo.objects.all()
        serializer = CargorSerializer(queryset, many=True)
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
        serializer = CargorSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            response["count"] = len(serializer.data)
            response["success"] = True
        return Response(response)


class OrderAPIView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
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
        print(data)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            response["count"] = len(serializer.data)
            response["success"] = True
        return Response(response)
