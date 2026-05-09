from rest_framework.viewsets import ModelViewSet
from books.pagination import StandardPagination
from books.permissions import IsAdminOrAuthenticatedReadOnly
from .models import Library
from .serializers import LibrarySerializer
from .services import get_coordinates


class LibraryViewSet(ModelViewSet):
    """
    API для библиотек.
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    pagination_class = StandardPagination
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    filterset_fields = ("is_active", )
    search_fields = ("name", "address", "description",)
    ordering_fields = ("name", "created_at",)

    def perform_create(self, serializer):
        """
        Автоматически получает координаты при создании библиотеки.
        """
        address = serializer.validated_data.get("address")
        latitude, longitude = get_coordinates(address)
        serializer.save(latitude=latitude, longitude=longitude)

    def perform_update(self, serializer):
        """
        Обновляет координаты при изменении адреса.
        """
        address = serializer.validated_data.get("address", serializer.instance.address,)
        latitude, longitude = get_coordinates(address)
        serializer.save(latitude=latitude, longitude=longitude)

