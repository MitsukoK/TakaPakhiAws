from django.contrib import admin
from django.urls import path
from .views import home, TestPage

urlpatterns = [
    path("", home, name="home"),
    path("test/", TestPage.as_view(), name="test"),
    # path("api/", include("api.urls")),
]
