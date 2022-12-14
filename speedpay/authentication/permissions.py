from rest_framework.permissions import BasePermission


class IsAuthenticatedOrAnonCreate(BasePermission):
    """Permission class which provides anonymous users with the power to create"""

    def has_permission(self, request, view):
        if view.action == "create" and request.user.is_anonymous:
            return True
        return bool(request.user and request.user.is_authenticated)
