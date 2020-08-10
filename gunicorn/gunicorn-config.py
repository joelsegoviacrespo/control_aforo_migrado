# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
import multiprocessing

#bind = '0.0.0.0:5005'
bind = 'unix:/tmp/gunicorn.sock'
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = './access.log'  #'-'
loglevel = './error.log'   #'debug'
reload = True
#daemon = True
capture_output = True
enable_stdio_inheritance = True
