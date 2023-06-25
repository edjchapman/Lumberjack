from django.contrib import admin
from django.urls import path, include, re_path

admin.site.site_title = "Lumberjack"
admin.site.site_header = "Lumberjack"


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api-auth/", include("rest_framework.urls")),
    path(r"api/", include("logs.urls")),
]
