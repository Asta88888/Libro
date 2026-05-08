from rest_framework.serializers import ModelSerializer
from .models import BookCopy

class BookCopySerializer(ModelSerializer):
    class Meta:
        model = BookCopy
        fields = "__all__"
        read_only_fields = ("created_at",)
