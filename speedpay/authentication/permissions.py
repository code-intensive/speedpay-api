from rest_framework.permissions import BasePermission


class IsAuthenticatedOrAnonCreate(BasePermission):
    """Permission class which provides anonymous users with the power to create."""

    def has_permission(self, request, view) -> bool:
        if view.action == "create" and request.user.is_anonymous:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj) -> bool:
        return (
            request.user == obj.speedpay_user
            or request.user.is_admin
            or request.user.is_superuser
        )


class IsAdminUserOrNoList(BasePermission):
    """Protects list action, only grants view to admin or super user."""

    def has_permission(self, request, view) -> bool:
        if view.action == "list":
            return request.user and (request.user.is_admin or request.user.is_superuser)
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj) -> bool:
        return (
            request.user == obj.speedpay_user
            or request.user.is_admin
            or request.user.is_superuser
        )
