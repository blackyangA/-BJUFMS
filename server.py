#! /usr/bin/env python3.9
# -*- coding: utf8 -*-

from waitress import serve
from app_main.wsgi import application


if __name__ == '__main__':
    serve(application, port='8000')
