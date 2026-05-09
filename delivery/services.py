from .models import Delivery


class DeliveryError(Exception):
    pass


def create_delivery(
        *,
        borrowing,
        user,
        address_source="user",
        custom_address=None
):
    """
    Создание доставки.
    """

    if hasattr(borrowing, "delivery"):
        raise DeliveryError("Доставка уже существует.")

    if address_source == "user":
        address = user.address

        if not address:
            raise DeliveryError(
                "У пользователя не указан адрес."
            )

    elif address_source == "custom":

        if not custom_address:
            raise DeliveryError(
                "Не указан адрес доставки."
            )

        address = custom_address

    else:
        raise DeliveryError(
            "Неверный источник адреса."
        )

    return Delivery.objects.create(
        borrowing=borrowing,
        user=user,
        address_source=address_source,
        address=address,
    )


def update_delivery_status(delivery, status_value: str):
    """
    Обновление статуса доставки.
    """

    valid_statuses = [
        choice[0]
        for choice in Delivery.Status.choices
    ]

    if status_value not in valid_statuses:
        raise DeliveryError("Неверный статус.")

    delivery.status = status_value
    delivery.save(
        update_fields=["status", "updated_at"]
    )

    return delivery
