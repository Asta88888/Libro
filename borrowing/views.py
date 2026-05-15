from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Borrowing
from .serializers import BorrowingSerializer
from .services import borrow_book, return_book, BorrowingError

from inventory.models import BookCopy

from books.pagination import StandardPagination
from .permissions import IsAdminOrOwner


class BorrowingViewSet(ModelViewSet):
    serializer_class = BorrowingSerializer
    permission_classes = [IsAdminOrOwner]
    pagination_class = StandardPagination

    filterset_fields = ("status", "user")
    search_fields = (
        "book_copy__book__title",
        "user__email",
    )
    ordering_fields = (
        "borrowed_at",
        "due_date",
        "status",
    )

    def get_queryset(self):
        user = self.request.user

        if getattr(self, "swagger_fake_view", False):
            return Borrowing.objects.none()

        if user.is_staff:
            return Borrowing.objects.select_related(
                "user",
                "book_copy",
                "book_copy__book",
            )

        return Borrowing.objects.filter(
            user=user
        ).select_related(
            "user",
            "book_copy",
            "book_copy__book",
        )

    @action(detail=False, methods=["post"])
    def borrow(self, request):
        try:
            book_copy_id = request.data.get("book_copy_id")
            days = int(request.data.get("days", 14))

            if not book_copy_id:
                return Response(
                    {"error": "book_copy_id обязателен"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            book_copy = BookCopy.objects.get(id=book_copy_id)

            borrowing = borrow_book(
                user=request.user,
                book_copy=book_copy,
                days=days
            )

            return Response(
                BorrowingSerializer(borrowing).data,
                status=status.HTTP_201_CREATED
            )

        except BookCopy.DoesNotExist:
            return Response(
                {"error": "Экземпляр книги не найден"},
                status=404
            )

        except BorrowingError as e:
            return Response(
                {"error": str(e)},
                status=400
            )

    @action(detail=True, methods=["post"])
    def return_book(self, request, pk=None):
        try:
            borrowing = self.get_object()

            result = return_book(borrowing)

            return Response(
                BorrowingSerializer(result).data,
                status=status.HTTP_200_OK
            )

        except BorrowingError as e:
            return Response(
                {"error": str(e)},
                status=400
            )