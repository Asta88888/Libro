from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import BookViewSet, AuthorViewSet, GenreViewSet


app_name = "books"

router = SimpleRouter()

router.register(r"books", BookViewSet, basename="books")
router.register(r"authors", AuthorViewSet, basename="authors")
router.register(r"genres", GenreViewSet, basename="genres")

urlpatterns = [
    path("", include(router.urls)),
]
