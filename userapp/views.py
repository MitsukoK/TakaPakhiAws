from django.urls.exceptions import Http404
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_401_UNAUTHORIZED)
from rest_framework.views import APIView

from banking.models import BankingMethod
from userapp.models import NewUser
from userapp.serializer import ChangePinSerializer, NewUserSerializer

# Create your views here.


class LogoutView(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)


class UserView(APIView):
    def get(self, req):
        return Response("user page", status=HTTP_200_OK)


# get user details
class UserDetailView(APIView):
    def get(self, req):
        # check if user is authenticated
        if req.user.is_authenticated:
            # get the user details
            _user = NewUser.objects.filter(username=req.user.username)
            # _user = NewUser.objects.get(id=req.user.id)
            print("this is user", _user.values()[0])
            serializer = NewUserSerializer(_user, many=True)

            return Response(serializer.data, status=HTTP_200_OK)
            # return Response("user details", status=HTTP_200_OK)

        return Response("user not authenticated", status=HTTP_200_OK)


class UserBankView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        if req.user.is_authenticated:
            # get the user details
            # _user = NewUser.objects.filter(username=req.user.username)
            # print(_user.bank)
            # return _user.values("bank")
            # return Response(_user.values("bank"), status=HTTP_200_OK)
            _user = NewUser.objects.get(id=req.user.id)
            # get the bank details
            _bank = _user.bank
            _banking_detail = [
                BankingMethod.objects.get(name=recharge, types="Bank")
                for recharge in _bank
            ]

            json_data = []
            # now add the data to json
            for i in range(len(_banking_detail)):
                data = {
                    "name": _banking_detail[i].name,
                    "logo": _banking_detail[i].logo.url,
                    "type": _banking_detail[i].types,
                }
                json_data.append(data)
            # json_data[i] = {
            #     _banking_detail[i].name,
            #     _banking_detail[i].logo.url,
            #     _banking_detail[i].types,
            # }
            # return _bank as response
            return Response(json_data, status=HTTP_200_OK)


class UserRechargeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        if req.user.is_authenticated:
            # get the user details
            # _user = NewUser.objects.filter(username=req.user.username)
            # print(_user.mobile_recharge)
            # return _user.values("mobile_recharge")
            # return Response(_user.values("mobile_recharge"), status=HTTP_200_OK)
            _user = NewUser.objects.get(id=req.user.id)
            # get the bank details
            _mobile_recharge = _user.mobile_recharge  # List<String>

            _banking_detail = [
                BankingMethod.objects.get(name=recharge, types="Mobile Recharge")
                for recharge in _mobile_recharge
            ]

            json_data = []
            # now add the data to json
            for i in range(len(_banking_detail)):
                data = {
                    "name": _banking_detail[i].name,
                    "logo": _banking_detail[i].logo.url,
                    "type": _banking_detail[i].types,
                }
                json_data.append(data)
            # json_data[i] = {
            #     _banking_detail[i].name,
            #     _banking_detail[i].logo.url,
            #     _banking_detail[i].types,
            # }
            # print("banking details -> ", json_data)
            # return _bank as response
            return Response(json_data, status=HTTP_200_OK)


class UserMobileBankView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        if req.user.is_authenticated:
            # get the user details
            # _user = NewUser.objects.filter(username=req.user.username)
            # print(_user.mobile_banking)
            # return _user.values("mobile_banking")
            # return Response(_user.values("mobile_banking"), status=HTTP_200_OK)
            _user = NewUser.objects.get(id=req.user.id)
            # mobile bnak
            _mobile_banking = _user.mobile_banking
            _banking_detail = [
                BankingMethod.objects.get(name=recharge, types="Mobile Banking")
                for recharge in _mobile_banking
            ]

            json_data = []
            # now add the data to json
            for i in range(len(_banking_detail)):
                data = {
                    "name": _banking_detail[i].name,
                    "logo": _banking_detail[i].logo.url,
                    "type": _banking_detail[i].types,
                }
                json_data.append(data)

            return Response(json_data, status=HTTP_200_OK)


class UserCurrentBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        if req.user.is_authenticated:
            _user = NewUser.objects.get(id=req.user.id)
            # current balance
            _current_balance = _user.current_balance
            return Response(_current_balance, status=HTTP_200_OK)


class UserFullDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        if req.user.is_authenticated:
            # get the user details
            # _user = NewUser.objects.filter(username=req.user.username)
            # print(_user)
            # return _user.values()
            # return Response(_user.values(), status=HTTP_200_OK)
            _user = NewUser.objects.get(id=req.user.id)
            # current balance
            _full_details = _user
            return Response(_full_details, status=HTTP_200_OK)


# class UserChangePinView(ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = ChangePinSerializer

#     def get_queryset(self):
#         return NewUser.objects.filter(id=self.request.user.id)


class UserChangePinView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePinSerializer

    def get_queryset(self):
        return NewUser.objects.filter(id=self.request.user.id)

    def put(self, req):
        if req.user.is_authenticated:
            _user = NewUser.objects.get(id=req.user.id)
            serializer = ChangePinSerializer(data=req.data)
            if serializer.is_valid():
                old_pin = serializer.data.get("old_pin")
                new_pin = serializer.data.get("new_pin")
                current_pin = _user.user_pin
                if old_pin == current_pin:
                    _user.user_pin = new_pin
                    _user.save()
                    return Response("Pin Changed", status=HTTP_200_OK)
                elif old_pin != current_pin:
                    return Response("Old Pin is incorrect", status=HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
