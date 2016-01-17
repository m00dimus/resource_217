#// ------------------------------------
#// Title: resource_datetime.py
#// Description: Common datetime functions
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160116 (python 3.4.3)
#// ------------------------------------

import time
import datetime

def get_current_timestamp():
    dformat='%Y-%m-%d %H:%M:%S'
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime(dformat)
    return st

def get_current_date():
    dformat='%Y-%m-%d'
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime(dformat)
    return st

def get_current_time():
    dformat='%H:%M:%S'
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime(dformat)
    return st