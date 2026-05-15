from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User

        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone",
            "date_of_birth",
            "role",
            "image",
            "address",
            "bio",
            "is_student",
            "is_active_reader",
            "date_joined",
            "latitude",
            "longitude",
        )

        read_only_fields = (
            "id",
            "role",
            "date_joined",
            "latitude",
            "longitude",
        )

