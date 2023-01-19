from rest_framework import permissions 

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    A custom permission to only allow the owners of the snippet to edit or delete them
    """ 

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # That means only the GET, HEAD, and OPTIONS requests are allowed
        if request.methods in permissions.SAFE_METHODS:
            return True
        # The CREATE, PATCH and DELETE are allowed to the owner
        return obj.owner == request.user