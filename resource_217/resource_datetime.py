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

def get_current_formal_date():
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%A, %B %d, %Y')
	return st

def get_formated_timestamp(dvalue,sDateFormat='%Y-%m-%d %H:%M:%S'):
    result = datetime.datetime.fromtimestamp(dvalue).strftime(sDateFormat)
    return result
    
def isvaliddate(sValue,sDateFormat='%Y-%m-%d %H:%M:%S'):
    try:
        datetime.datetime.strptime(sValue, sDateFormat)
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD HH:mm:ss")
        return False
    return True

def gettimestampoffset(sValue,sDateFormat='%Y-%m-%d %H:%M:%S',d=0,s=0):
    if isvaliddate(sValue,sDateFormat):
        sCurrentValue = datetime.datetime.strptime(sValue, sDateFormat)
        sOffestValue = sCurrentValue + datetime.timedelta(days=d,seconds=s)
        result = sOffestValue.strftime(sDateFormat)
        return result
    else:
        return False
