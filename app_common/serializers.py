#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'first_name', 'last_name', 'username', 'password', 'email', 'is_active', 'groups',
                  'is_staff', 'is_superuser']

    def validate_password(self, data):
        passhash = make_password(data)
        return passhash


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
