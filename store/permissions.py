from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS requests for all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Check if the user is the owner of the profile
        return obj.user == request.user


class IsAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_superuser
