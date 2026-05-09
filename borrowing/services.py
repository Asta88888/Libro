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
        raise BorrowingError("Эта книга уже выдана или недоступна")

    if Borrowing.objects.filter(user=user, book_copy=book_copy, status=Borrowing.Status.ACTIVE).exists():
        raise BorrowingError("У вас уже есть активная выдача этой книги")

    borrowing = Borrowing.objects.create(user=user, book_copy=book_copy, due_date=timezone.now() + timedelta(days=days),
                                         )
    book_copy.status = BookCopy.Status.BORROWED
    book_copy.save(update_fields=["status"])
    return borrowing

@transaction.atomic
def return_book(borrowing: Borrowing):
    """
    Возврат книги.
    """
    if borrowing.returned_at:
        raise BorrowingError("Эта книга уже возвращена")

    borrowing.returned_at = timezone.now()

    borrowing.update_status()
    borrowing.save(update_fields=["returned_at", "status"])

    book_copy = borrowing.book_copy
    book_copy.status = BookCopy.Status.AVAILABLE
    book_copy.save(update_fields=["status"])

    return borrowing
