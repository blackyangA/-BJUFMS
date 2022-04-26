#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from rest_framework import serializers


class AuditSerializer(serializers.Serializer):      # noqa
    created_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.IntegerField(source='created_by.id', read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)
    modified_by = serializers.IntegerField(source='modified_by.id', read_only=True)
