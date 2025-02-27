from django.urls import path
from classes.views import home

urlpatterns = [
    path("", home, name="home"),
]
