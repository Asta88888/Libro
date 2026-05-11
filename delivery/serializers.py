from rest_framework.serializers import ModelSerializer
from .models import Delivery

class DeliverySerializer(ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"
        read_only_fields = ("id", "user", "created_at", "updated_at",)

