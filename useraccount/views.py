from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import ListView
from .forms import NewUserForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator
from user_request.models import (
    BankingModel,
    RequestMobileBankModel,
    RequestMobileRechargeModel,
)


# def login(request):
#     # if post method is called
#     if request.method == "POST":
#         print("post method called in login\n\n\n\n")
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("dashboard_items")

#     return render(request, "login_form.html", {})


# def register(request):
#     return render(request, "register_form.html", {})


# def register_request(request):
#     if request.method == "POST":
#         print("post method called")
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             print("form is valid")
#             # user = form.save()
#             form.save()
#             # login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect("home")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
#     return render(
#         request,
#         "register_form.html",
#         context={"register_form": form},
#     )


class LoginView(View):
    template_name = "login_form.html"

    # @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard_items")
        return render(request, self.template_name, {})

    # @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard_items")

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, "User Does Not Exist")
            return render(request, self.template_name, {})
        elif not user.is_active:
            messages.warning(request, "User is not active")
            return render(request, self.template_name, {})
        elif not user.check_password(password):
            messages.error(request, "Invalid Password")
            return render(request, self.template_name, {})
        else:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("dashboard_items")
        # if forum.is_valid():
        #     print("form is valid", forum.cleaned_data, "\n\n\n\n")
        #     # cleaned_data = forum.cleaned_data
        #     cleaned_data = forum.clean()
        #     print(cleaned_data)
        #     # user = form.save()
        #     forum.save()
        #     # login(request, user)
        #     messages.success(request, "Login successful.")
        #     return redirect("dashboard_items")
        # elif forum.errors:
        #     _e = forum.errors.as_data()
        #     messages.error(request, _e["__all__"][0])
        return render(request, self.template_name, {})


class RegisterFormView(View):
    form_class = NewUserForm
    template_name = "register_form.html"
    success_url = "/"

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        # form = self.form_class(None)
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        print("post method called")
        form = self.form_class(request.POST)
        if form.is_valid():
            print("form is valid and saved\n\n\n\n\n")
            form.save()
            return redirect(self.success_url)
        else:

            print("form is invalidddddddddddddddddddddddddd\n\n\n\n")
            # print form.errors
            print(form.errors.as_data())
        # return super(RegisterFormView, self).post(request, *args, **kwargs)
        return render(request, self.template_name, {"form": form})


def logouth(request):
    # logout the user
    logout(request)
    return render(request, "index.html", {})


class DashboardView(View):
    template_name = "dashboard_items.html"
    # use all models form the user_request app
    # model = BankingModel

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login_form")

        context = {
            "MobileBank": RequestMobileBankModel.objects.all().order_by("-id")[:10],
            "MobileRecharge": RequestMobileRechargeModel.objects.all().order_by("-id")[
                :10
            ],
            "Banking": BankingModel.objects.all().order_by("-id")[:10],
            # "GiftCard": BankingModel.objects.all().order_by("-id")[:10],
        }
        return render(request, self.template_name, context)


# def dashboard(request):
#     if not request.user.is_superuser:
#         return redirect("login_form")
#     # return render(request, self.template_name, {})

#     context = {
#         "MobileBank": RequestMobileBankModel.objects.all().order_by("-id")[:10],
#         "MobileRecharge": RequestMobileRechargeModel.objects.all().order_by("-id")[:10],
#         "Banking": BankingModel.objects.all().order_by("-id")[:10],
#         "GiftCard": BankingModel.objects.all().order_by("-id")[:10],
#     }

#     return render(request, "dashboard_items.html", context)


class MobileRechargeView(View):
    template_name = "mobile_recharge.html"
    # use all models form the user_request app
    model = RequestMobileRechargeModel

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login_form")

        context = {
            "MobileRecharge": RequestMobileRechargeModel.objects.all().order_by("-id")[
                :10
            ],
            # "GiftCard": BankingModel.objects.all().order_by("-id")[:10],
        }
        return render(request, self.template_name, context)


class MobileBankView(View):
    template_name = "mobile_bank.html"
    # use all models form the user_request app
    # model = RequestMobileBankModel

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login_form")

        context = {
            "MobileRecharge": RequestMobileBankModel.objects.all().order_by("-id")[:10],
            # "GiftCard": BankingModel.objects.all().order_by("-id")[:10],
        }
        return render(request, self.template_name, context)


class BankView(View):
    template_name = "bank_view.html"
    # use all models form the user_request app
    # model = BankingModel

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login_form")

        context = {
            "MobileRecharge": BankingModel.objects.all().order_by("-id")[:10],
            # "GiftCard": BankingModel.objects.all().order_by("-id")[:10],
        }
        return render(request, self.template_name, context)
