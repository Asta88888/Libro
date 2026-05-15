from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import LibraryViewSet

router = SimpleRouter()
router.register(r"", LibraryViewSet, basename="libraries")

urlpatterns = [
    path("", include(router.urls))
]