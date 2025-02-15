#!/usr/bin/python
# -*- coding: utf-8 -*-

from csv import Error
import platform
import subprocess
from longpool import job_longpool
import logging
import os

try:
    os.chdir("D:/Dmitry/NIRFI_server_bot")
except Error as err:
    logging.info(err)

logging.basicConfig(filename = 'logs.log',  filemode='a', level = logging.INFO, format = ' %(asctime)s - %(levelname)s - %(message)s', encoding = "UTF-8", datefmt='%d-%b-%y %H:%M:%S')

logging.info('Бот запущен...')

if __name__ == '__main__':
    job_longpool()
