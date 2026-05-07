from rest_framework.viewsets import ModelViewSet
from .models import Book, Genre, Author
from .serializers import BookSerializer, GenreSerializer, AuthorSerializer

class BookViewSet(ModelViewSet):
    """
    API для работы с книгами.
    Поддерживает CRUD операции.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GenreViewSet(ModelViewSet):
    """
    API для работы с жанрами.
    Поддерживает CRUD операции.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class AuthorViewSet(ModelViewSet):
    """
    API для работы с авторами.
    Поддерживает CRUD операции.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

