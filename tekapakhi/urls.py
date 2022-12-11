from django.conf.urls.static import static  # new
from django.contrib import admin
from django.urls import include, path

from tekapakhi import settings

admin.site.site_header = "Takapakhi Admin"
admin.site.index_title = "Admin"

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
