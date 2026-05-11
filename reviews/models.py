from django.db import models
from books.models import Book
from users.models import User

class Review(models.Model):
    """
    Отзыв пользователя о книге.
    """
    class Rating(models.IntegerChoices):
        ONE = 1, "1"
        TWO = 2, "2"
        THREE = 3, "3"
        FOUR = 4, "4"
        FIVE = 5, "5"

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews", verbose_name="Книга")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", verbose_name="Пользователь")
    rating = models.PositiveSmallIntegerField(choices=Rating.choices, verbose_name="Рейтинг")
    text = models.TextField(verbose_name="Отзыв", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]
        unique_together = ("book", "user")

    def __str__(self):
        return f"{self.book.title} - {self.user.email} ({self.rating})"
