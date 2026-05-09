from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    """
    Разрешение только для администраторов.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsAuthenticatedAndReadOnly(BasePermission):
    """
    Разрешает просмотр только авторизованным пользователям.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.method in SAFE_METHODS
        )

class IsAdminOrAuthenticatedReadOnly(BasePermission):
    """
    Администратор может изменять данные.
    Авторизованные пользователи могут только читать.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return (
                request.user
                and request.user.is_authenticated
            )
        return (
            request.user
            and request.user.is_staff
        )