from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Borrowing
from .serializers import BorrowingSerializer
from .services import borrow_book, return_book, BorrowingError
from inventory.models import BookCopy

class BorrowingViewSet(ModelViewSet):
    """
    API для выдачи и возврата книг.
    """
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

    @action(detail=False, methods=["post"])
    def borrow(self, request):
        """
        Выдать книгу пользователю.
        """
        try:
            book_copy_id = request.data.get("book_copy_id")
            days = int(request.data.get("days", 14))

            book_copy = BookCopy.objects.get(id=book_copy_id)

            borrowing = borrow_book(user=request.user, book_copy=book_copy, days=days)
            return Response(BorrowingSerializer(borrowing).data, status=status.HTTP_201_CREATED)
        except BookCopy.DoesNotExist:
            return Response(
                {"error": "Книга не найдена"},
                status=status.HTTP_404_NOT_FOUND
            )
        except BorrowingError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=True, methods=["post"])
    def return_book(self, request, pk=None):
        """
        Возврат книги.
        """
        try:
            borrowing = self.get_object()
            borrowing = return_book(borrowing)

            return Response(BorrowingSerializer(borrowing).data, status=status.HTTP_200_OK)
        except BorrowingError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
