from django.db import models
from borrowing.models import Borrowing
from users.models import User

class Delivery(models.Model):
    """
    Доставка выданной книги пользователю.
    """
    class AddressSource(models.TextChoices):
        USER = "user", "Из профиля пользователя"
        CUSTOM = "custom", "Введен вручную"

    class Status(models.TextChoices):
        PENDING = "pending", "Ожидает"
        IN_PROGRESS = "in_progress", "В пути"
        DELIVERED = "delivered", "Доставлено"
        CANCELED = "canceled", "Отменено"

    borrowing = models.OneToOneField(Borrowing, on_delete=models.CASCADE, related_name="delivery", verbose_name="Выдача")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deliveries", verbose_name="Пользователь")
    address_source = models.CharField(max_length=10, choices=AddressSource.choices, default=AddressSource.USER)
    address = models.CharField(max_length=300, verbose_name="Адрес доставки")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING, verbose_name="Статус доставки")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Delivery #{self.id} ({self.user.email})"
