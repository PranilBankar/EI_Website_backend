# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RegistrationViewSet, api_login

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="event")
router.register(r"registrations", RegistrationViewSet, basename="registration")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/login/", api_login, name="api_login"),
]
