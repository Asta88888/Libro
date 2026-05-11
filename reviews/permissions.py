from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdminReadOnly(BasePermission):
    """
    - GET: все авторизованные
    - POST/PUT/DELETE: только владелец или админ
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user
