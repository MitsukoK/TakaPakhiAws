from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from userapp.views import (
    LogoutView,
    UserBankView,
    UserCurrentBalanceView,
    UserDetailView,
    UserMobileBankView,
    UserRechargeView,
)

# from .views import MobileRecharge, MobileBank, Bank

urlpatterns = [
    #! user app URLS
    path("user/", UserDetailView.as_view(), name="userdetailview"),
    path("user/login/", obtain_auth_token, name="login"),
    path("user/logout/", LogoutView.as_view(), name="logout"),
    path("user/bank/", UserBankView.as_view(), name="user_bank"),
    path("user/recharge/", UserRechargeView.as_view(), name="user_recharge"),
    path("user/mobile_bank/", UserMobileBankView.as_view(), name="user_mobile_bank"),
    path(
        "user/current_balance/",
        UserCurrentBalanceView.as_view(),
        name="user_current_balance",
    ),
]
