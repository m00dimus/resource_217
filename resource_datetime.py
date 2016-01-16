#// ------------------------------------
#// Title: resource_crypto.py
#// Description: Common datetime functions
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160116 (python 3.4.3)
#// ------------------------------------

import time
import datetime

def get_current_timestamp():
    ts = time.time()

    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st

def get_current_date():
    ts = time.time()

    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    return st

def get_current_time():
    ts = time.time()

    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    return st


