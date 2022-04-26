#! /usr/bin/env python3.9
# -*- coding: utf8 -*-


import logging

from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.middleware import AuthenticationMiddleware

from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication

logger = logging.getLogger(__name__)


def get_user_jwt(request):
    """
    Replacement for django session auth get_user & auth.get_user
     JSON Web Token authentication. Inspects the token for the user_id,
     attempts to get that user from the DB & assigns the user on the
     request object. Otherwise it defaults to AnonymousUser.

    This will work with existing decorators like LoginRequired  ;)

    Returns: instance of user object or AnonymousUser object
    """
    user = None
    try:
        user_jwt = JWTAuthentication().authenticate(Request(request))
        if user_jwt is not None:
            # store the first part from the tuple (user, obj)
            user = user_jwt[0]
    except Exception as e:
        logger.exception(e)
        pass

    return user or AnonymousUser()


class JWTAuthenticationMiddleware(MiddlewareMixin):
    """ Middleware for authenticating JSON Web Tokens in Authorize Header """
    def process_request(self, request):
        if 'Authorization' in request.headers:
            request.user = SimpleLazyObject(lambda: get_user_jwt(request))
