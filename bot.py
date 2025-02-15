#!/usr/bin/python
# -*- coding: utf-8 -*-

import platform
import subprocess
from longpool import job_longpool
import logging
import os

try:
    os.chdir("D:/Dmitry/NIRFI_server_bot")
except:
    logging.info('Не сменил')

def ping_ip(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    with open(os.devnull, 'w') as devnull:
        if subprocess.call(command, stdout=devnull, stderr=devnull) == 0:
            print(f"{ip} is active")

ping_ip(f"10.0.0.137")


logging.basicConfig(filename = 'logs.log',  filemode='a', level = logging.INFO, format = ' %(asctime)s - %(levelname)s - %(message)s', encoding = "UTF-8", datefmt='%d-%b-%y %H:%M:%S')

logging.info('Бот запущен...')

if __name__ == '__main__':
    job_longpool()
