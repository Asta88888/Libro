from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import BorrowingViewSet

router = SimpleRouter()
router.register(r"", BorrowingViewSet, basename="borrowings")

urlpatterns = [
    path("", include(router.urls)),
]