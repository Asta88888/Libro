from rest_framework.permissions import BasePermission

class IsAdminOrOwner(BasePermission):
    """
    Администратор видит всё.
    Пользователь — только свои выдачи.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_staff
            or obj.user == request.user
        )
