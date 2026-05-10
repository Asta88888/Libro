from .models import Review

class ReviewError(Exception):
    pass

def create_or_update_review(*, user, book, rating, text=""):
    """
    Один пользователь = один отзыв на книгу.
    """
    review, created = Review.objects.update_or_create(user=user, book=book, defaults={"rating": rating, "text": text,},)
    return review
