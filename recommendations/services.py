from django.db.models import Avg, Count
from books.models import Book
from reviews.models import Review


def get_recommendations_for_user(user, limit=10):
    """
    Генерация рекомендаций книг для пользователя.
    """

    user_book_ids = Review.objects.filter(
        user=user
    ).values_list("book_id", flat=True)

    user_genres = Review.objects.filter(
        user=user
    ).values_list("book__genres__id", flat=True)

    books = (
        Book.objects
        .exclude(id__in=user_book_ids)
        .prefetch_related("genres")
        .annotate(
            avg_rating=Avg("reviews__rating"),
            reviews_count=Count("reviews", distinct=True),
            borrow_count=Count("copies__borrowings", distinct=True),
        )
    )

    scored_books = []

    for book in books:
        score = 0

        if book.avg_rating:
            score += float(book.avg_rating) * 2

        score += min(book.reviews_count * 0.3, 3)
        score += min(book.borrow_count * 0.2, 3)

        book_genre_ids = set(
            book.genres.values_list("id", flat=True)
        )

        if book_genre_ids.intersection(set(user_genres)):
            score += 3

        scored_books.append((score, book))

    scored_books.sort(
        key=lambda x: x[0],
        reverse=True,
    )

    return [
        book
        for score, book
        in scored_books[:limit]
    ]