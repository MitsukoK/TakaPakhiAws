from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def home(req):
    return render(req, "index.html", {})


class TestPage(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        return Response("You are valid", status=HTTP_200_OK)
