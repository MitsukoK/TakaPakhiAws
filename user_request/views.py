from django.shortcuts import render
from rest_framework.decorators import api_view

# from rest_framework import mixins
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


# from ..useraccount.forms import RequestForm
from .models import RequestMobileBankModel, RequestMobileRechargeModel, BankingModel
from .serializations import (
    RequestMobileBankSerializer,
    RequestMobileRechargeSerializer,
    BankingSerializer,
)

# Create your views here.


def request_home(request):
    return render(request, "request.html")


@api_view(["GET"])
def request_list(request):

    context = {
        "MobileBank": RequestMobileBankModel.objects.all().order_by("-id")[:10],
        "MobileRecharge": RequestMobileRechargeModel.objects.all().order_by("-id")[:10],
        "Banking": BankingModel.objects.all().order_by("-id")[:10],
        "GiftCard": BankingModel.objects.all().order_by("-id")[:10],
    }

    return render(request, "request.html", context)


# @api_view(["POST"])
# def post_request(request):
#     if request.method == "POST":
#         form = RequestForm(request.POST)
#         # rendered_form = form.render("form_snippet.html")
#         if form.is_valid():
#             # form.save()
#             print("form is valid", form.cleaned_data)
#             return render(request, "thanks.html")
#     else:
#         form = RequestForm()

#     return render(request, "request_form.html", {"form": form})


# def get_post_requst(request):
#     if request.method == "POST":
#         form = RequestForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             return render(request, "request_form.html")
#         # redirect to a new URL: request_form.html
#         return render(request, "request_form.html")
#     return render(request, "request_form.html")

# post request to the database


class MobileBankingView(ListCreateAPIView):
    """This class handles the http GET and POST requests."""

    permission_classes = (IsAuthenticated,)
    queryset = RequestMobileBankModel.objects.all()
    serializer_class = RequestMobileBankSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        # get the user from the request
        _user = self.request.user
        # now add the user to the serializer
        serializer.save(user=_user)
        # serializer.save()

    def get_queryset(self):
        """This view should return a list of all the purchases
        for the currently authenticated user."""
        user = self.request.user
        return RequestMobileBankModel.objects.filter(user=user)


class MobileRechargeView(ListCreateAPIView):
    """This class handles the http GET and POST requests."""

    permission_classes = (IsAuthenticated,)
    queryset = RequestMobileRechargeModel.objects.all()
    serializer_class = RequestMobileRechargeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        # get the user from the request
        _user = self.request.user
        # now add the user to the serializer
        serializer.save(user=_user)
        # serializer.save()

    def get_queryset(self):
        """This view should return a list of all the purchases
        for the currently authenticated user."""
        user = self.request.user
        return RequestMobileRechargeModel.objects.filter(user=user)


class BankingView(ListCreateAPIView):
    """This class handles the http GET and POST requests."""

    permission_classes = (IsAuthenticated,)
    queryset = BankingModel.objects.all()
    serializer_class = BankingSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        # get the user from the request
        _user = self.request.user
        # now add the user to the serializer
        serializer.save(user=_user)
        # serializer.save()

    def get_queryset(self):
        """This view should return a list of all the purchases
        for the currently authenticated user."""
        user = self.request.user
        return BankingModel.objects.filter(user=user)
