from datetime import timedelta
from django.utils import timezone
from django.db import transaction

from inventory.models import BookCopy
from borrowing.models import Borrowing
from delivery.services import create_delivery


class BorrowingError(Exception):
    pass


@transaction.atomic
def borrow_book(*, user, book_copy: BookCopy, days: int = 14):
    """
    Выдача книги + автоматическая доставка
    """

    if book_copy.status != BookCopy.Status.AVAILABLE:
        raise BorrowingError("Экземпляр недоступен")

    if Borrowing.objects.filter(
        user=user,
        book_copy=book_copy,
        status=Borrowing.Status.ACTIVE
    ).exists():
        raise BorrowingError("Уже выдано")

    borrowing = Borrowing.objects.create(
        user=user,
        book_copy=book_copy,
        due_date=timezone.now() + timedelta(days=days),
        status=Borrowing.Status.ACTIVE
    )

    book_copy.status = BookCopy.Status.BORROWED
    book_copy.save(update_fields=["status"])

    create_delivery(
        borrowing=borrowing,
        user=user,
        address_source="user"
    )

    return borrowing


def return_book(*, borrowing: Borrowing):
    """
    Возврат книги
    """

    if borrowing.returned_at:
        raise BorrowingError("Книга уже возвращена")

    borrowing.returned_at = timezone.now()
    borrowing.status = Borrowing.Status.RETURNED
    borrowing.save(update_fields=["returned_at", "status"])

    copy = borrowing.book_copy
    copy.status = BookCopy.Status.AVAILABLE
    copy.save(update_fields=["status"])

    return borrowing
