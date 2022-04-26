#! /usr/bin/env python3.9
# -*- coding: utf8 -*-

from rest_framework import permissions


class DjangoModelStrictPermission(permissions.DjangoModelPermissions):
    """
    严格 Django Model Permission
    Get 方法需要有对应的view 权限
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
        )
