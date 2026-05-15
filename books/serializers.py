from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import Author, Genre, Book


class AuthorSerializer(ModelSerializer):
    """
    Сериализатор автора.
    """

    full_name = SerializerMethodField()

    def get_full_name(self, obj):
        first = obj.first_name or ""
        last = obj.last_name or ""

        return f"{first} {last}".strip()

    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ("id",)


class GenreSerializer(ModelSerializer):
    """
    Сериализатор жанра.
    """

    class Meta:
        model = Genre
        fields = "__all__"
        read_only_fields = ("id",)


class BookSerializer(ModelSerializer):
    """
    Сериализатор книги.
    """

    author = AuthorSerializer(read_only=True)
    genres = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
        )