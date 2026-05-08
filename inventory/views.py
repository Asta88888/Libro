from rest_framework.viewsets import ModelViewSet
from .models import BookCopy
from .serializers import BookCopySerializer
from books.permissions import IsAdminOrAuthenticatedReadOnly
from books.pagination import StandardPagination

class BookCopyViewSet(ModelViewSet):
    """
    API для управления экземплярами книг.
    """
    queryset = BookCopy.objects.select_related("book", "library",)
    serializer_class = BookCopySerializer
    pagination_class = StandardPagination
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    filterset_fields = ("status", "book", "library",)
    search_fields = ("inventory_number", "book__title", "library__name",)
    ordering_fields = ("created_at", "inventory_number", "status",)
