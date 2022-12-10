from django.urls import path
from .views import login, logouth, RegisterFormView, DashboardView, dashboard

urlpatterns = [
    # path("", UserView.as_view(), name="userview"),
    path("login/", login, name="login_form"),
    path("logout/", logouth, name="logout_form"),
    # path("register/", register_request, name="register_form"), # RegisterFormView
    path(
        "register/", RegisterFormView.as_view(), name="register_form"
    ),  # RegisterFormView
    # path("dashboard/", DashboardView.as_view(), name="dashboard_items"),
    path("dashboard/", dashboard, name="dashboard_items"),
]
