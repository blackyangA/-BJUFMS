#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from django.db import models
from django.conf import settings
from middleware.current_user import get_current_user


class CreationAuditMixin(models.Model):
    """
    审计操作行为
    """
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   editable=False,
                                   related_name='+',
                                   default=get_current_user)

    class Meta:
        abstract = True


class ModificationAuditMixin(models.Model):
    """
    审计更新行为
    """
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    editable=False,
                                    related_name='+',
                                    default=get_current_user)

    class Meta:
        abstract = True
        
    def save(self, current_user=None, *args, **kwargs):
        if current_user:
            self.modified_by = current_user
        else:
            self.modified_by = get_current_user()
        super(ModificationAuditMixin, self).save(*args, **kwargs)


class FullAuditMixin(ModificationAuditMixin, CreationAuditMixin):
    """
    全量操作审计
    """
    class Meta:
        abstract = True
        