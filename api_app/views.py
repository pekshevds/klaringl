from django.http import HttpRequest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication


class CheckConnectionAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        response: dict = dict()
        return Response(response, status=status.HTTP_200_OK)
