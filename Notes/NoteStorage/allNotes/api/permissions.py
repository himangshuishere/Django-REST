from http.client import REQUEST_URI_TOO_LONG
from rest_framework import permissions


class NoteUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user