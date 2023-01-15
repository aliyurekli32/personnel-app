from rest_framework import permissions

class IsStafforReadOnly(permissions.IsAdminUser):
    message = 'You do not have permission perform this action.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
        
class IsOwnerAndStafforReadOnly(permissions.BasePermission):
   def has_object_permissions(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
           return True
       return bool(request.user.is_staff and (obj.create_user==request.user))