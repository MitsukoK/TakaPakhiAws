from rest_framework.serializers import ModelSerializer

from .models import FundModel, OfferModel


class OfferSerializer(ModelSerializer):
    class Meta:
        model = OfferModel
        fields = "__all__"


class FundSerializer(ModelSerializer):
    class Meta:
        model = FundModel

        # fields = "__all__"
        exclude = ["id", "user"]
