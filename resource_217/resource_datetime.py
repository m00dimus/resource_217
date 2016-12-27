#// ------------------------------------
#// Title: resource_datetime.py
#// Description: Common datetime functions
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160116 (python 3.4.3)
#// ------------------------------------

import time
import datetime

def get_current_timestamp(sDateFormat='%Y-%m-%d %H:%M:%S'):
    '''
    Get current timestamp.
    '''
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime(sDateFormat)
    return st

def get_current_date(sDateFormat='%Y-%m-%d'):
    '''
    Get current date.
    '''
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime(sDateFormat)
    return st

def get_current_time(sDateFormat='%H:%M:%S'):
    '''
    Get current time.

    If sDateFormat is specified then result will be returned in that format.

    '''
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime(sDateFormat)
    return st

def datediff(d1,d2,sDateFormat='%Y-%m-%d %H:%M:%S',seconds=True,minutes=False,hours=False,days=False):
    '''
    Get differences between two dates in days, hours, minutes, or seconds. The default result type is seconds.

    If sDateFormat is specified then other date formats can be processed.
    '''
    if type(d1) == str:
        d1=datetime.datetime.strptime(d1,sDateFormat).timestamp()
    if type(d2) == str:
        d2=datetime.datetime.strptime(d2,sDateFormat).timestamp()
    if seconds:
        typevalue=1
    if minutes:
        typevalue=60
    if hours:
        typevalue=60*60
    if days:
        typevalue=60*60*24
    result = abs((d2-d1)/typevalue)
    return result

def get_current_formal_date():
    '''
    Get current timestamp in formal format of '%A, %B %d, %Y'.
    '''
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%A, %B %d, %Y')
    return st

def get_formated_timestamp(dvalue,sDateFormat='%Y-%m-%d %H:%M:%S'):
    '''
    Input a datavalue and return a formated timestamp.

    If sDateFormat is specified then other date formats can be processed.
    '''
    result = datetime.datetime.fromtimestamp(dvalue).strftime(sDateFormat)
    return result

def isvaliddate(d1,sDateFormat='%Y-%m-%d %H:%M:%S'):
    '''
    Input a datevalue and check if it is valid.

    If sDateFormat is specified then other date formats can be processed.

    It’s common for this to be restricted to years from 1970 through 2038.
    '''
    #print('IsValid:' + str(type(d1)))
    try:
        if type(d1)==str:
            #// convert string to float
            d1=datetime.datetime.strptime(d1,sDateFormat).timestamp()
            #print('IsValid:' + 'converted string to float')
        if type(d1)==datetime.datetime:
            #// convert datetime to float
            d1=time.mktime(d1)
            #print('IsValid:' + 'converted datetime to float')

        if d1 > 0.0 and d1 < 2145938400.0:
            return True
        else:
            return False
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD HH:mm:ss")
        return False
    return False

def gettimestampoffset(d1,sDateFormat='%Y-%m-%d %H:%M:%S',days=0,seconds=0):
    '''
    Input a valid datevalue and return an offset timestamp. Both positive and negative offsets for days and/or seconds are accepted.

    If sDateFormat is specified then other date formats can be processed.
    '''
    if isvaliddate(d1,sDateFormat):
        try:
            if type(d1)==str:
                #// convert string to float
                d1=datetime.datetime.strptime(d1,sDateFormat)#.timestamp()
                #print('gettimestampoffset:' + 'converted string to float')
            if type(d1)==datetime.datetime:
                d2 = d1 + datetime.timedelta(days=days,seconds=seconds)
                result = d2.strftime(sDateFormat)
                return result
        except:
            return False
    else:
        #// invalid date
        return False
