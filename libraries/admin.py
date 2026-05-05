from django.contrib import admin
from .models import Library
from .services import get_coordinates

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "latitude", "longitude", "is_active")
    search_fields = ("name", "address")
    list_filter = ("is_active",)
    readonly_fields = ("latitude", "longitude", "created_at")

    def save_model(self, request, obj, form, change):
        """
        Автоматически получает координаты при сохранении библиотеки.
        """
        if obj.address and (obj.latitude is None or obj.longitude is None):
            lat, lon = get_coordinates(obj.address)
            obj.latitude = lat
            obj.longitude = lon
        super().save_model(request, obj, form, change)
