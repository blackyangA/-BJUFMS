#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
import logging
from threading import local
_local_logger = local()


class LevelEqFilter(object):
    """
    过滤指定 level 的log
    """
    def __init__(self, level):
        self.__level = level

    def filter(self, log_record):
        return log_record.levelno == self.__level


class ThreadLocalLoggingHandler(logging.Handler):
    def __init__(self):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Our custom argument
        _local_logger.log_list = []
        self.log_list = _local_logger.log_list

    def emit(self, record):
        # record.message is the log message
        self.log_list.append(self.format(record))

    def pop_log(self):
        ret = self.log_list
        self.log_list = []
        return ret
