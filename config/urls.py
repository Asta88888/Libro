from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Libro API",
        default_version="v1",
        description="Library management system API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/users/", include(("users.urls", "users"), namespace="users")),
    path("api/books/", include(("books.urls", "books"), namespace="books")),
    path("api/libraries/", include(("libraries.urls", "libraries"), namespace="libraries")),
    path("api/inventory/", include(("inventory.urls", "inventory"), namespace="inventory")),
    path("api/borrowing/", include(("borrowing.urls", "borrowing"), namespace="borrowing")),
    path("api/delivery/", include(("delivery.urls", "delivery"), namespace="delivery")),
    path("api/reviews/", include(("reviews.urls", "reviews"), namespace="reviews")),

    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
