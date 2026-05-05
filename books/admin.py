from django.contrib import admin
from .models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "years_of_life")
    search_fields = ("first_name", "last_name")
    list_filter = ("years_of_life",)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "publish_date", "created_at", )
    search_fields = ("title", "author__first_name", "author__last_name", "isbn")
    list_filter = ("genres", "publish_date")
    filter_horizontal = ("genres",)
    autocomplete_fields = ("author",)
