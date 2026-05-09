from django.contrib import admin
from .models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "address_source", "created_at",)
    list_filter = ("status", "address_source",)
    search_fields = ("user__email", "address",)
    ordering = ("-created_at",)

