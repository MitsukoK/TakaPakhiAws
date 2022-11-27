from rest_framework.serializers import ModelSerializer
from .models import RequestMobileBankModel, RequestMobileRechargeModel, BankingModel


class RequestMobileBankSerializer(ModelSerializer):
    class Meta:
        model = RequestMobileBankModel
        # fields = "__all__"
        exclude = [
            "user",
        ]


class RequestMobileRechargeSerializer(ModelSerializer):
    class Meta:
        model = RequestMobileRechargeModel
        # fields = "__all__"
        exclude = [
            "user",
        ]


class BankingSerializer(ModelSerializer):
    class Meta:
        model = BankingModel
        # fields = "__all__"
        exclude = [
            "user",
        ]
