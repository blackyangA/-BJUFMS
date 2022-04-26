#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_query_param = 'page'
    page_size_query_param = 'pageSize'
