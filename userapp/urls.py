from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LogoutView, UserDetailView, UserView

urlpatterns = [
    path("", UserDetailView.as_view(), name="userdetailview"),
    path("login/", obtain_auth_token, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
