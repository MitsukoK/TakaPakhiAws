from django.shortcuts import render, redirect
from django.contrib.auth import logout
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

# Create your views here.


def login(request):
    # return render(request, "index.html")

    return render(request, "login_form.html", {})


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


# def dashboard(request):
#     return render(request, "dashboard_items.html", {})


class DashboardView(ListView):
    template_name = "dashboard_items.html"
    # use all models form the user_request app
    model = BankingModel

    # def get(self, request, *args, **kwargs):
    #     if not request.user.is_superuser:
    #         return redirect("login_form")
    #     return render(request, self.template_name, {})

    # def post(self, request, *args, **kwargs):
    #     if not request.user.is_superuser:
    #         return redirect("login_form")
    #     return render(request, self.template_name, {})
