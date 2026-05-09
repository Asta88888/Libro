from rest_framework.serializers import ModelSerializer
from .models import Author, Genre, Book

class AuthorSerializer(ModelSerializer):
    """
    Сериализатор автора.
    Используется для отображения и создания авторов.
    """
    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ("id",)

class GenreSerializer(ModelSerializer):
    """
    Сериализатор жанра.
    Используется для работы с жанрами книг.
    """
    class Meta:
        model = Genre
        fields = "__all__"
        read_only_fields = ("id",)

class BookSerializer(ModelSerializer):
    """
    Сериализатор книги.
    Позволяет получать, создавать и обновлять книги.
    """
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ("id", "created_at")
