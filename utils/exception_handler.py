#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from rest_framework.views import exception_handler
from rest_framework.exceptions import PermissionDenied


def antd_exception_handler(exc, context):
    """
    Antd UMI request 风格异常处理接口

    interface ErrorInfoStructure {
      success: boolean; // if request is success
      data?: any; // response data
      errorCode?: string; // code for errorType
      errorMessage?: string; // message display to user
      showType?: number; // error display type： 0 silent; 1 message.warn; 2 message.error; 4 notification; 9 page
      traceId?: string; // Convenient for back-end Troubleshooting: unique request ID
      host?: string; // Convenient for backend Troubleshooting: host of current access server
    }

    :param exc:
    :param context:
    :return:
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        resp = {
            'success': False,
            'errorCode': getattr(exc, 'error_code', '10000'),
            'errorMessage': getattr(exc, 'error_message', None) or response.data.get('detail') or 'field validation error',
            'showType': getattr(exc, 'show_type', 1),
            'traceId': '',
            'host': '',
        }
        response.data = resp

    return response
