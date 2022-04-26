#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
import logging

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from utils.permission import ReadOnly
from .models import DocumentFileModel, AccountingFileModel, PhysicalFileModel, ElectronicFileModel
from .serializers import DocumentFileSerializer, AccountingFileSerializer, PhysicalFileSerializer, \
    ElectronicFileSerializer

logger = logging.getLogger(__name__)


class DocumentFileViewSet(ModelViewSet):
    """
    文书档案 DocumentFile
    """
    queryset = DocumentFileModel.objects.all()
    serializer_class = DocumentFileSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class AccountingFileViewSet(ModelViewSet):
    """
    会计档案 AccountingFile
    """
    queryset = AccountingFileModel.objects.all()
    serializer_class = AccountingFileSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class PhysicalFileViewSet(ModelViewSet):
    """
    实物档案 PhysicalFile
    """
    queryset = PhysicalFileModel.objects.all()
    serializer_class = PhysicalFileSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]


class ElectronicFileViewSet(ModelViewSet):
    """
    电子档案 ElectronicFile
    """
    queryset = ElectronicFileModel.objects.all()
    serializer_class = ElectronicFileSerializer
    permission_classes = [permissions.IsAdminUser | (ReadOnly & permissions.IsAuthenticated)]
