from django.urls import path
from .views import (
    LoginView,
    login,
    logouth,
    RegisterFormView,
    DashboardView,
    MobileRechargeView,
    BankView,
    MobileBankView,
)

urlpatterns = [
    # path("", UserView.as_view(), name="userview"),
    # path("login/", login, name="login_form"),
    path("login/", LoginView.as_view(), name="login_form"),
    path("logout/", logouth, name="logout_form"),
    # path("register/", register_request, name="register_form"), # RegisterFormView
    path(
        "register/", RegisterFormView.as_view(), name="register_form"
    ),  # RegisterFormView
    path("dashboard/", DashboardView.as_view(), name="dashboard_items"),
    path("recharge/", MobileRechargeView.as_view(), name="recharge_view"),
    path("mobile_bank/", MobileBankView.as_view(), name="mobilebank"),
    path("bank/", MobileRechargeView.as_view(), name="bankview"),
]
