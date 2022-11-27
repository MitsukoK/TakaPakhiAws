from django.urls import path
from .views import (
    request_home,
    # post_request,
    request_list,
    MobileBankingView,
    MobileRechargeView,
    BankingView,
)

urlpatterns = [
    # path("", index, name="req_index"),
    path("", request_home, name="req_index"),
    # path("form/", post_request, name="post_request"),
    path("list/", request_list, name="request_list"),
    path("mobilebanking/", MobileBankingView.as_view(), name="mobilebanking"),
    path("mobilercharge/", MobileRechargeView.as_view(), name="mobilercharge"),
    path("banking/", BankingView.as_view(), name="banking"),
]
