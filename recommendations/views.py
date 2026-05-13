from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from books.pagination import StandardPagination
from books.serializers import BookSerializer

from .services import get_recommendations_for_user


class RecommendationView(APIView):
    """
    Персональные рекомендации книг.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = get_recommendations_for_user(
            request.user
        )

        paginator = StandardPagination()

        page = paginator.paginate_queryset(
            books,
            request,
        )

        serializer = BookSerializer(
            page,
            many=True,
        )

        return paginator.get_paginated_response(
            serializer.data
        )
