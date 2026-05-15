from django.db import models
from books.models import Book
from libraries.models import Library


class BookCopy(models.Model):
    """
    Конкретный экземпляр книги в библиотеке.
    """

    class Status(models.TextChoices):
        AVAILABLE = "available", "Доступна"
        RESERVED = "reserved", "Забронирована"
        BORROWED = "borrowed", "Выдана"
        IN_TRANSIT = "in_transit", "В пути"
        DAMAGED = "damaged", "Повреждена"
        LOST = "lost", "Утеряна"

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="copies",
        verbose_name="Книга"
    )

    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name="book_copies",
        verbose_name="Библиотека"
    )

    inventory_number = models.CharField(
        max_length=50,
        verbose_name="Инвентарный номер"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
        verbose_name="Статус"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Экземпляр книги"
        verbose_name_plural = "Экземпляры книги"
        ordering = ["book", "library"]
        unique_together = ("library", "inventory_number")

    def __str__(self):
        return f"{self.book.title} — {self.inventory_number} ({self.library.name})"