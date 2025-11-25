from django.urls import path
from .views import send_email
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("send-email/", send_email),
    path("sign-in/",ObtainAuthToken.as_view())
]
