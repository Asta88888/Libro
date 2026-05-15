from .models import Delivery


class DeliveryError(Exception):
    pass


def create_delivery(*, borrowing, user, address_source="user", custom_address=None):

    if hasattr(borrowing, "delivery"):
        return borrowing.delivery

    if address_source == "user":
        address = getattr(user, "address", None)
        if not address:
            raise DeliveryError("Нет адреса у пользователя")

    elif address_source == "custom":
        if not custom_address:
            raise DeliveryError("Нет custom адреса")
        address = custom_address

    else:
        raise DeliveryError("Неверный address_source")

    return Delivery.objects.create(
        borrowing=borrowing,
        user=user,
        address_source=address_source,
        address=address,
    )


def update_delivery_status(delivery, status_value: str):
    valid = [c[0] for c in Delivery.Status.choices]

    if status_value not in valid:
        raise DeliveryError("Неверный статус")

    delivery.status = status_value
    delivery.save(update_fields=["status", "updated_at"])
    return delivery
