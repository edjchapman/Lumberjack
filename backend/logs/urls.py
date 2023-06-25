from django.urls import include, path
from rest_framework import routers

from logs import views

router = routers.DefaultRouter()
router.register(r"logs", views.ExceptionLogViewSet)

urlpatterns = [path("", include(router.urls))]
