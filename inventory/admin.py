from django.contrib import admin
from .models import BookCopy

@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "library", "inventory_number", "status", "created_at",)
    list_filter = ("status", "library")
    search_fields = ("inventory_number", "book__title", "library__name")
    autocomplete_fields = ("book", "library")
    readonly_fields = ("created_at",)
