from django.contrib import admin
from django.urls import path, include
from tekapakhi import settings
from django.conf.urls.static import static  # new

urlpatterns = [
    path("", include("landing.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("user/", include("userapp.urls")),
    path("account/", include("useraccount.urls")),
    path("request/", include("user_request.urls")),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
