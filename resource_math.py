#// ------------------------------------
#// Title: resource_math.py
#// Description: Common math functions
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160114
#// ------------------------------------

def isprime(n):
    '''
    Check if number is prime
    '''
    #// accept only integers
    if not isinstance(n,int):
        return False
    #// evaluate the absolute value
    n=abs(n)
    #// not 0 or 1
    if n < 2:
        return False
    #// 2 is the only even prime
    if n == 2:
        return True
    #// not even 
    if n%2 == 0:
        return False
    #// only odds that are not prime
    for x in range(3,int(n**0.5+1)):
        if n%x==0:
            return False
    #// is prime
    return True

def iseven(n):
    '''
    Check if number is even
    '''
    #// accept only integers
    if not isinstance(n,int):
        return False
    if n%2 == 0:
        return True
    return False

def isodd(n):
    '''
    Check if number is odd
    '''
    #// accept only integers
    if not isinstance(n,int):
        return False
    if n%2 == 1:
        return True
    return False



    
