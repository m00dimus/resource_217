#// ------------------------------------
#// Title: resource_string.py
#// Description: Common string functions
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160114
#// ------------------------------------

def isconsonant(s):
    '''
    Check if character is a consonant
    '''
    #// accept only strings with length of 1
    if not isinstance(s,str) or len(s) > 1:
        return False
    #// accept only characters that are not vowels
    if s.isalpha() and s.lower() not in ['a','e','i','o','u']:
        return True
    return False

def isvowel(s):
    '''
    Check if character is a vowel
    '''
    #// accept only strings with length of 1
    if not isinstance(s,str) or len(s) > 1:
        return False
    #// accept only characters that are vowels
    if s.isalpha() and s.lower() in ['a','e','i','o','u']:
        return True
    return False
