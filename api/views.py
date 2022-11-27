# from rest_framework.response import Response
# from rest_framework.views import APIView
# from banking.models import BankingMethod
# from .serializations import (
#     MobileRechargeSerializer,
#     BankSerializer,
#     MobileBankSerializer,
# )


# class MobileRecharge(APIView):
#     """
#     Mobile recharge api

#     """

#     def get(self, req):
#         """get request from mr"""
#         all_objects = BankingMethod.objects.filter(types__name="Mobile Recharge")
#         # data = list(all_objects.values)
#         serializer = MobileRechargeSerializer(all_objects, many=True)
#         return Response(serializer.data)


# class MobileBank(APIView):
#     """
#     Mobile recharge api

#     """

#     def get(self, req):
#         """get request from mr"""
#         all_objects = BankingMethod.objects.filter(types__name="Mobile Banking")
#         # data = list(all_objects.values)
#         serializer = MobileBankSerializer(all_objects, many=True)
#         return Response(serializer.data)


# class Bank(APIView):
#     """
#     Mobile recharge api

#     """

#     def get(self, req):
#         """get request from mr"""
#         all_objects = BankingMethod.objects.filter(types__name="Bank")
#         # data = list(all_objects.values)
#         serializer = BankSerializer(all_objects, many=True)
#         return Response(serializer.data)
