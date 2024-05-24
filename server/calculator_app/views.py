from django.http import HttpRequest, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (
    permissions,
    authentication
)
from calculator_app.models import City, Rate
from calculator_app.serializers import CitySerializer, RateSerializer


class CityView(APIView):

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


class RateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> HttpResponse:
        queryset = Rate.objects.all()
        serializer = RateSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)
