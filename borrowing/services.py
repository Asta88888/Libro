from datetime import timedelta
from django.utils import timezone
from django.db import transaction
from inventory.models import BookCopy
from borrowing.models import Borrowing

class BorrowingError(Exception):
    pass

@transaction.atomic
def borrow_book(user, book_copy: BookCopy, days: int = 14):
    """
    Выдача книги пользователю.
    """
    if book_copy.status != BookCopy.Status.AVAILABLE:
        raise BorrowingError("Книга недоступна")

    due_date = timezone.now() + timedelta(days=days)

    borrowing = Borrowing.objects.create(user=user, book_copy=book_copy, due_date=due_date,)
    book_copy.status = BookCopy.Status.BORROWED
    book_copy.save()
    return borrowing

@transaction.atomic
def return_book(borrowing: Borrowing):
    """
    Возврат книги.
    """
    if borrowing.status == Borrowing.Status.RETURNED:
        raise BorrowingError("Книга уже возвращена")

    borrowing.returned_at = timezone.now()
    borrowing.status = Borrowing.Status.RETURNED
    borrowing.save()

    book_copy = borrowing.book_copy
    book_copy.status = BookCopy.Status.AVAILABLE
    book_copy.save()

    return borrowing
