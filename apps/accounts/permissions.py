from rest_framework import permissions


class GroupMemberPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, group):
        return group.users.filter(id=request.user.id).exists()
