#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    class Meta:
        ordering = ('id',)
