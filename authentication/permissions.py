from rest_framework.permissions import BasePermission


class IsSuper(BasePermission):
    """Grants client admins full access"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "('SUPER',)"  


class IsAdmin(BasePermission):
    """Grants client admins full access"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"
              
              
              
class IsClientAdmin(BasePermission):
    """Grants client admins full access"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'client_admin'


class IsOwnerOrAdmin(BasePermission):
    """Grants client admins full access"""

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.role == 'admin' or request.user == obj.client_admin


class IsProfileOwner(BasePermission):
    """allow only profile owners to update profiles"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
