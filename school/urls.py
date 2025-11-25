from rest_framework.routers import DefaultRouter
from school.viewsets import SchoolViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("",SchoolViewSet, basename="school")


urlpatterns = [
    path("", include(router.urls))
]
