#// ------------------------------------
#// Title: resource_string.py
#// Description: Common string functions
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160114
#// ------------------------------------
import re

def isconsonant(s=''):
    """ Check if character is a consonant """
    #// accept only strings with length of 1
    if not isinstance(s,str) or len(s) > 1:
        return False
    #// accept only characters that are not vowels
    if s.isalpha() and s.lower() not in ['a','e','i','o','u']:
        return True
    return False

def isvowel(s=''):
    """ Check if character is a vowel """
    #// accept only strings with length of 1
    if not isinstance(s,str) or len(s) > 1:
        return False
    #// accept only characters that are vowels
    if s.isalpha() and s.lower() in ['a','e','i','o','u']:
        return True
    return False

def stringspacing(sValue='',doublespace=False):
    """ Enforce standard spacing through a string. """
    result=sValue

    #// force polyspace to single space
    while "  " in result:
        result=result.replace("  "," ")

    #// remove leading space
    if result.startswith(" "):
        result=result[1:]

    #// override to doublespace
    if doublespace:
        result=result.replace(" ","  ")

    return result

def suppressleadingzeros(sValue=''):
    """ Suppress leading zeros in string """
    result=sValue

    searchstr=re.compile("(\w(\s)?)+")
    #// evalulate word in string
    if re.match(searchstr,result):
        resultlist=sValue.split(' ')
        result=[]
        for item in resultlist:
            while item[:1] == "0":
                item=item[1:]
            result.append(item)
        result=" ".join(result)

    return result
