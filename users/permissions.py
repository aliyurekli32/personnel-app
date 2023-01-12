from rest_framework import permissions

class IsOwnerStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_staff or (obj.user ==request.user))