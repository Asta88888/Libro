from rest_framework.serializers import ModelSerializer
from .models import Borrowing

class BorrowingSerializer(ModelSerializer):
    """
    Сериализатор книг.
    """
    class Meta:
        model = Borrowing
        fields = "__all__"
        read_only_fields = ("id", "borrowed_at", "returned_at", "status",)
