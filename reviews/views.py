from rest_framework.viewsets import ModelViewSet

from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsOwnerOrAdminReadOnly
from .services import create_or_update_review
from books.pagination import StandardPagination


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = StandardPagination
    permission_classes = [IsOwnerOrAdminReadOnly]

    filterset_fields = ("rating", "book")
    search_fields = ("text", "book__title", "user__email")
    ordering_fields = ("created_at", "rating")

    def get_queryset(self):
        user = self.request.user
        qs = Review.objects.select_related("book", "user")
        if user.is_staff:
            return qs
        if not user.is_authenticated:
            return qs.none()
        return qs.filter(user=user)
    def perform_create(self, serializer):
        review = create_or_update_review(user=self.request.user,
                                         book=serializer.validated_data["book"],
                                         rating=serializer.validated_data["rating"],
                                         text=serializer.validated_data.get("text", ""),
                                         )
        serializer.instance = review
