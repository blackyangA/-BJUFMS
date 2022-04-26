#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from rest_framework import serializers
from .models import DocumentFileModel, AccountingFileModel, PhysicalFileModel, ElectronicFileModel


class DocumentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentFileModel
        fields = '__all__'


class AccountingFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingFileModel
        fields = '__all__'


class PhysicalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalFileModel
        fields = '__all__'


class ElectronicFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicFileModel
        fields = '__all__'
