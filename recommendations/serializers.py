from rest_framework.serializers import ModelSerializer

from books.serializers import BookSerializer
from .models import Recommendation


class RecommendationSerializer(ModelSerializer):
    """
    Сериализатор рекомендаций.
    """

    book = BookSerializer(read_only=True)

    class Meta:
        model = Recommendation
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
        )