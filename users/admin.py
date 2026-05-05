from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("id", "email", "first_name", "last_name", "role", "is_active")
    list_filter = ("role", "is_active", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("id",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Личная информация", {
            "fields": ("first_name", "last_name", "phone", "date_of_birth", "image", "bio")
        }),
        ("Адрес и гео", {
            "fields": ("address", "latitude", "longitude")
        }),
        ("Статус", {
            "fields": ("role", "is_active", "is_staff", "is_superuser", "is_student", "is_active_reader")
        }),
        ("Даты", {
            "fields": ("date_joined",)
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )
    readonly_fields = ("date_joined",)
    filter_horizontal = ()
