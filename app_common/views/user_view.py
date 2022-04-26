#! /usr/bin/env python3.9
# -*- coding: utf8 -*-

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from app_main import permissions
from utils.permission import ReadOnly
from app_common.serializers import UserSerializer, GroupSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]

    def get_queryset(self):
        """
        Determine if the user is admin, if yes return all, not then return rules with status 1
        """
        print(self.request.user)
        if self.request.user.is_staff:
            return User.objects.all()
        id = self.request.user.id
        return User.objects.filter(id=id)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]
        return [permission() for permission in permission_classes]

    def get_object(self):
        if self.kwargs['pk'] == 'me':
            return self.request.user
        return super(UserViewSet, self).get_object()

    def retrieve(self, request, *args, **kwargs):
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
