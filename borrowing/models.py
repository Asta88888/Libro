from django.db import models
from django.utils import timezone
from users.models import User
from inventory.models import BookCopy
from django.db.models import Q

class Borrowing(models.Model):
    """
    Выдача книг пользователю.
    """
    class Status(models.TextChoices):
        ACTIVE = "active", "Активна"
        RETURNED = "returned", "Возвращена"
        OVERDUE = "overdue", "Просрочена"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrowings", verbose_name="Пользователь")
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, related_name="borrowings", verbose_name="Экземпляр книги")
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(verbose_name="Дата возврата")
    returned_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE, verbose_name="Статус")

    class Meta:
        verbose_name = "Выдача книги"
        verbose_name_plural = "Выдача книг"
        ordering = ["-borrowed_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["book_copy"],
                condition=Q(status="active"),
                name="unique_active_borrowing_per_copy"
            )
        ]

    def __str__(self):
        return f"{self.user.email} → {self.book_copy} ({self.status})"

    @property
    def is_overdue(self):
        return (
            self.due_date < timezone.now()
            and self.status != self.Status.RETURNED
        )

    @property
    def days_left(self):
        return (self.due_date - timezone.now()).days
