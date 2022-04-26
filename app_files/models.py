#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from django.db import models
from utils.audit_model import FullAuditMixin
from django.utils.translation import gettext_lazy as _


class DocumentFileModel(FullAuditMixin):
    """
    文书档案 DocumentFile
    """

    text = models.TextField(_('原文'), null=True, editable=False)
    file_no = models.CharField(_('案卷级档号'), max_length=255, null=True, editable=False)
    title = models.CharField(_('题名'), max_length=255, null=True, editable=False)
    all_sovereign = models.IntegerField(_('全宗号'), blank=True, editable=False, default=0)
    ecn = models.CharField(_('实体分类号'), max_length=255, null=True, editable=False)
    catalogue_no = models.IntegerField(_('目录号'), blank=True, editable=False, default=0)
    case_file_no = models.IntegerField(_('案卷号'), blank=True, editable=False, default=0)
    start_dt = models.DateField(_('文件开始时间'), null=True, blank=True, editable=False)
    end_dt = models.DateField(_('文件结束时间'), null=True, blank=True, editable=False)
    total_pages = models.IntegerField(_('文件总页数'), blank=True, editable=False, default=0)
    poc = models.CharField(_('保管期限'), max_length=255, null=True, editable=False)

    class Meta:
        ordering = ('-id',)


class AccountingFileModel(FullAuditMixin):
    """
    会计档案 AccountingFile
    """

    text = models.TextField(_('原文'), null=True, editable=False)
    file_no = models.CharField(_('案卷级档号'), max_length=255, null=True, editable=False)
    title = models.CharField(_('题名'), max_length=255, null=True, editable=False)
    all_sovereign = models.IntegerField(_('全宗号'), blank=True, editable=False, default=0)
    ecn = models.CharField(_('实体分类号'), max_length=255, null=True, editable=False)
    catalogue_no = models.IntegerField(_('目录号'), blank=True, editable=False, default=0)
    case_file_no = models.IntegerField(_('案卷号'), blank=True, editable=False, default=0)
    start_dt = models.DateField(_('文件开始时间'), null=True, blank=True, editable=False)
    end_dt = models.DateField(_('文件结束时间'), null=True, blank=True, editable=False)
    total_pages = models.IntegerField(_('文件总页数'), blank=True, editable=False, default=0)
    poc = models.CharField(_('保管期限'), max_length=255, null=True, editable=False)

    class Meta:
        ordering = ('-id',)


class PhysicalFileModel(FullAuditMixin):
    """
    实物档案 PhysicalFile
    """

    text = models.TextField(_('原文'), null=True, editable=False)
    file_no = models.CharField(_('案卷级档号'), max_length=255, null=True, editable=False)
    title = models.CharField(_('题名'), max_length=255, null=True, editable=False)
    all_sovereign = models.IntegerField(_('全宗号'), blank=True, editable=False, default=0)
    ecn = models.CharField(_('实体分类号'), max_length=255, null=True, editable=False)
    catalogue_no = models.IntegerField(_('目录号'), blank=True, editable=False, default=0)
    case_file_no = models.IntegerField(_('案卷号'), blank=True, editable=False, default=0)
    start_dt = models.DateField(_('文件开始时间'), null=True, blank=True, editable=False)
    end_dt = models.DateField(_('文件结束时间'), null=True, blank=True, editable=False)
    total_pages = models.IntegerField(_('文件总页数'), blank=True, editable=False, default=0)
    poc = models.CharField(_('保管期限'), max_length=255, null=True, editable=False)

    class Meta:
        ordering = ('-id',)


class ElectronicFileModel(FullAuditMixin):
    """
    电子档案 ElectronicFile
    """

    text = models.TextField(_('原文'), null=True, editable=False)
    file_no = models.CharField(_('案卷级档号'), max_length=255, null=True, editable=False)
    title = models.CharField(_('题名'), max_length=255, null=True, editable=False)
    all_sovereign = models.IntegerField(_('全宗号'), blank=True, editable=False, default=0)
    ecn = models.CharField(_('实体分类号'), max_length=255, null=True, editable=False)
    catalogue_no = models.IntegerField(_('目录号'), blank=True, editable=False, default=0)
    case_file_no = models.IntegerField(_('案卷号'), blank=True, editable=False, default=0)
    start_dt = models.DateField(_('文件开始时间'), null=True, blank=True, editable=False)
    end_dt = models.DateField(_('文件结束时间'), null=True, blank=True, editable=False)
    total_pages = models.IntegerField(_('文件总页数'), blank=True, editable=False, default=0)
    poc = models.CharField(_('保管期限'), max_length=255, null=True, editable=False)

    class Meta:
        ordering = ('-id',)
