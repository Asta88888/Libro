from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Delivery
from .serializers import DeliverySerializer
from borrowing.permissions import IsAdminOrOwner
from .services import create_delivery, update_delivery_status, DeliveryError
from borrowing.models import Borrowing
from books.pagination import StandardPagination

class DeliveryViewSet(ModelViewSet):
    """
    API доставка книг.
    """
    serializer_class = DeliverySerializer
    permission_classes = [IsAdminOrOwner]
    pagination_class = StandardPagination

    filterset_fields = ("status", "address_source",)
    search_fields = ("address", "user__email",)
    ordering_fields = ("created_at", "updated_at", "status",)

    def get_queryset(self):
        """
        Админ видит все доставки.
        Пользователь — только свои.
        """
        user = self.request.user
        queryset = Delivery.objects.select_related("user", "borrowing", "borrowing__book_copy",)
        if user.is_staff:
            return queryset
        if not user.is_authenticated:
            return queryset.none()
        return queryset.filter(user=user)

    @action(detail=False, methods=["post"])
    def create_from_borrowing(self, request):
        """
        Создать доставку из выдачи книг.
        """
        try:
            borrowing_id = request.data.get("borrowing_id")
            if not borrowing_id:
                return Response(
                    {"error": "borrowing_id обязателен"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            address_source = request.data.get("address_source", "user")
            custom_address = request.data.get("address")

            borrowing = Borrowing.objects.get(id=borrowing_id)
            if (
                not request.user.is_staff
                and borrowing.user != request.user
            ):
                return Response(
                    {"error": "Нет доступа"},
                    status=status.HTTP_403_FORBIDDEN
                )

            delivery = create_delivery(borrowing=borrowing, user=request.user, address_source=address_source, custom_address=custom_address,)

            return Response(DeliverySerializer(delivery).data,status=status.HTTP_201_CREATED)

        except Borrowing.DoesNotExist:
            return Response(
                {"error": "Borrowing не найден"},
                status=status.HTTP_404_NOT_FOUND
            )
        except DeliveryError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=True, methods=["post"])
    def set_status(self, request, pk=None):
        """
        Обновление статуса доставки(для админа/курьера).
        """
        try:
            delivery = self.get_object()

            status_value = request.data.get("status")

            if not status_value:
                return Response(
                    {"error": "status обязателен"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            delivery = update_delivery_status(
                delivery,
                status_value
            )

            return Response(
                DeliverySerializer(delivery).data,
                status=status.HTTP_200_OK
            )

        except DeliveryError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
