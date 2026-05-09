from django.contrib import admin
from .models import Borrowing


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "book_copy", "status", "borrowed_at", "due_date", "returned_at",)
    list_filter = ("status", "borrowed_at", "due_date",)
    search_fields = ("user__email", "book_copy__book__title",)
    autocomplete_fields = ("user", "book_copy")
    readonly_fields = ("borrowed_at",)

    @admin.display(description="Просрочено")
    def is_overdue(self, obj):
        return obj.is_overdue

