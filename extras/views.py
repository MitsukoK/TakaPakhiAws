from django.shortcuts import render
from rest_framework.decorators import api_view
# from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from extras.models import FundModel, OfferModel
from extras.serializations import FundSerializer, OfferSerializer


class OfferListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = OfferModel.objects.all()
    serializer_class = OfferSerializer


class FundListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FundSerializer

    def get_queryset(self):
        return FundModel.objects.filter(user=self.request.user)
