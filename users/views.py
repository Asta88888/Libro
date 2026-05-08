from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin, IsSelfOrAdmin

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        if self.action in ["list", "destroy"]:
            return [IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and user.role == "admin":
            return User.objects.all()

        return User.objects.filter(id=user.id)