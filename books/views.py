from rest_framework.viewsets import ModelViewSet
from .models import Book, Genre, Author
from .serializers import BookSerializer, GenreSerializer, AuthorSerializer
from .pagination import StandardPagination
from .permissions import IsAdminOrAuthenticatedReadOnly

class BookViewSet(ModelViewSet):
    """
    API для работы с книгами.
    Поддерживает CRUD операции.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardPagination
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    filterset_fields = ("author", "genres")
    search_fields = ("title", "description",)
    ordering_fields = ("title", "created_at", "publish_date",)

class GenreViewSet(ModelViewSet):
    """
    API для работы с жанрами.
    Поддерживает CRUD операции.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = StandardPagination
    permission_classes = [IsAdminOrAuthenticatedReadOnly]

class AuthorViewSet(ModelViewSet):
    """
    API для работы с авторами.
    Поддерживает CRUD операции.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StandardPagination
    permission_classes = [IsAdminOrAuthenticatedReadOnly]

