from django.db import models
from users.models import User
from books.models import Book

class Recommendation(models.Model):
    """
    Рекомендации для пользователя.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recommendations")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="recommended_to")
    score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"
        unique_together = ("user", "book")
        ordering = ["-score"]

    def __str__(self):
        return f"{self.user.email} -> {self.book.title}"
