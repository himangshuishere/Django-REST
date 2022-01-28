from http.client import REQUEST_URI_TOO_LONG
from rest_framework import permissions


class NoteUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
        # Check permissions for read-only request
            return True
        else:
        # Check permissions for write request
            return obj.author == request.user