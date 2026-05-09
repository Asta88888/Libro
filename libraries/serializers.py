from rest_framework.serializers import ModelSerializer
from .models import Library

class LibrarySerializer(ModelSerializer):
    """
    Сериализатор библиотек.
    """
    class Meta:
        model = Library
        fields = "__all__"
        read_only_fields = ("id", "created_at", "latitude", "longitude",)
