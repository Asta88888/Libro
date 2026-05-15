from django.db import models
from borrowing.models import Borrowing
from users.models import User


class Delivery(models.Model):

    class AddressSource(models.TextChoices):
        USER = "user", "Из профиля"
        CUSTOM = "custom", "Вручную"

    class Status(models.TextChoices):
        PENDING = "pending", "Ожидает"
        IN_PROGRESS = "in_progress", "В пути"
        DELIVERED = "delivered", "Доставлено"
        CANCELED = "canceled", "Отменено"

    borrowing = models.OneToOneField(
        Borrowing,
        on_delete=models.CASCADE,
        related_name="delivery"
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    address = models.CharField(max_length=300)

    address_source = models.CharField(
        max_length=10,
        choices=AddressSource.choices,
        default=AddressSource.USER
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery #{self.id}"