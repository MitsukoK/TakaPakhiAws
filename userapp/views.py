from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from userapp.models import NewUser
from userapp.serializer import NewUserSerializer

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
            # return _bank as response
            return Response(_bank, status=HTTP_200_OK)


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
            _mobile_recharge = _user.mobile_recharge
            # return _bank as response
            return Response(_mobile_recharge, status=HTTP_200_OK)


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
            return Response(_mobile_banking, status=HTTP_200_OK)


class UserCurrentBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        if req.user.is_authenticated:
            # get the user details
            # _user = NewUser.objects.filter(username=req.user.username)
            # print(_user.current_balance)
            # return _user.values("current_balance")
            # return Response(_user.values("current_balance"), status=HTTP_200_OK)
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
