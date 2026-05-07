from django.db import models
from django.utils import timezone
from users.models import User
from inventory.models import BookCopy

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

    borrowed_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата взятия")
    due_date = models.DateTimeField(verbose_name="Дата возврата")
    returned_at = models.DateTimeField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE, verbose_name="Статус")

    class Meta:
        verbose_name = "Выдача книги"
        verbose_name_plural = "Выдача книг"
        ordering = ["-borrowed_at"]


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

    def update_status(self):
        """
        Автоматически обновляет статус выдачи.
        """
        if self.returned_at:
            new_status = self.Status.RETURNED
        elif timezone.now() > self.due_date:
            new_status = self.Status.OVERDUE
        else:
            new_status = self.Status.ACTIVE
        if self.status != new_status:
            self.status = new_status
            self.save(update_fields=["status"])

