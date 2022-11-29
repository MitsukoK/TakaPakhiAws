from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    LogoutView,
    UserDetailView,
    # UserView,
    UserBankView,
    UserRechargeView,
    UserMobileBankView,
)

urlpatterns = [
    path("", UserDetailView.as_view(), name="userdetailview"),
    path("login/", obtain_auth_token, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("bank/", UserBankView.as_view(), name="user_bank"),
    path("recharge/", UserRechargeView.as_view(), name="user_recharge"),
    path("mobile_bank/", UserMobileBankView.as_view(), name="user_mobile_bank"),
]
