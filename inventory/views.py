from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from books.permissions import IsAdminOrAuthenticatedReadOnly
from books.pagination import StandardPagination

from books.models import Book
from libraries.models import Library
from inventory.models import BookCopy
from inventory.serializers import BookCopySerializer


class BookCopyViewSet(ModelViewSet):
    queryset = BookCopy.objects.select_related("book", "library")
    serializer_class = BookCopySerializer
    pagination_class = StandardPagination
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    filterset_fields = ("status", "book", "library")
    search_fields = ("inventory_number", "book__title", "library__name")
    ordering_fields = ("created_at", "inventory_number", "status")

    def get_queryset(self):
        qs = super().get_queryset()

        library_id = self.request.query_params.get("library")
        status = self.request.query_params.get("status")

        if library_id:
            qs = qs.filter(library_id=library_id)

        if status:
            qs = qs.filter(status=status)

        return qs


class CreateBookCopiesView(APIView):

    @transaction.atomic
    def post(self, request):
        book_id = request.data.get("book_id")
        library_id = request.data.get("library_id")
        count = int(request.data.get("count", 1))

        if not book_id or not library_id:
            return Response(
                {"error": "book_id и library_id обязательны"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            book = Book.objects.get(id=book_id)
            library = Library.objects.get(id=library_id)
        except Book.DoesNotExist:
            return Response({"error": "Book не найден"}, status=404)
        except Library.DoesNotExist:
            return Response({"error": "Library не найдена"}, status=404)

        created = []

        for i in range(count):
            copy = BookCopy.objects.create(
                book=book,
                library=library,
                inventory_number=f"{library.id}-{book.id}-{i+1}",
                status=BookCopy.Status.AVAILABLE
            )
            created.append(copy.id)

        return Response(
            {
                "message": "BookCopies created",
                "created_count": len(created),
                "ids": created
            },
            status=201
        )
