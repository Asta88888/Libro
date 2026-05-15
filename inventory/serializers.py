from rest_framework.serializers import ModelSerializer

from books.serializers import BookSerializer
from libraries.serializers import LibrarySerializer
from .models import BookCopy

class BookCopySerializer(ModelSerializer):
    book = BookSerializer(read_only=True)
    library = LibrarySerializer(read_only=True)

    class Meta:
        model = BookCopy
        fields = "__all__"
        read_only_fields = ("created_at",)
