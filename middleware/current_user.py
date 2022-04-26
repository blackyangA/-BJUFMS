#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
import logging
from threading import local
from django.utils.deprecation import MiddlewareMixin
logger = logging.getLogger(__name__)


_user = local()


class CurrentUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.debug(request.user)
        _user.value = request.user


def get_current_user():
    """
    :return: 当前用户
    """
    try:
        user = _user.value
    except AttributeError as e:
        user = None
    return user

