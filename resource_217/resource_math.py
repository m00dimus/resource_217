#// ------------------------------------
#// Title: resource_math.py
#// Description: Common math functions
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160114
#// ------------------------------------

import math
import random

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

def sumpowers(n,k):
    '''
    Result sum of integers raised to power k
    Optimized using forms found by Jacob Bernoulli as described
    in (Numerical Methods for Scientists and Engineers, Hamming, p185)
    Also known as Faulhaber's formula.
    '''
    if k == 1:
        result = ((n+1)*n)/2
        return int(result)
    elif k == 2:
        result = (n+1)*n*(2*n+1)/6
        return int(result)
    elif k == 3:
        result = pow(((n*(n+1))/2),2)
        return int(result)
    elif k == 4:
        result = (((n+1)*n*(2*n+1))/6)*((3*pow(n,2)+3*n-1)/5)
        return int(result)
    elif k == 5:
        result = pow(((n*(n+1))/2),2)*((2*pow(n,2)+2*n-1)/3)
        return int(result)
    elif k == 6:
        result = (((n+1)*n*(2*n+1))/6)*((3*pow(n,4)+6*pow(n,3)-3*n+1)/7)
        return int(result)
    elif k == 7:
        result = pow(((n*(n+1))/2),2)*((3*pow(n,4)+6*pow(n,3)-pow(n,2)-4*n+2)/6)
        return int(result)
    else:
        i=1
        result=0
        while i<=n:
            numsum=pow(i,k)
            result=result+numsum
            i=i+1
        return result

def vector2D_magnitude(aArray=[0,0],bArray=[0,0]):
    '''
    Return magnitude of a 2D vector
    '''
    result=math.sqrt((bArray[0]-aArray[0])**2 + (bArray[1]-aArray[1])**2)
    return result

def vector3D_magnitude(aArray=[0,0,0],bArray=[0,0,0]):
    '''
    Return magnitude of a 3D vector
    '''
    result=0
    result=math.sqrt((bArray[0]-aArray[0])**2 + (bArray[1]-aArray[1])**2 + (bArray[2]-aArray[2])**2)
    return result

def vector2D_random(floatvalue=False,LowValue=0,HighValue=1):
    '''
    Return a random 2D vector
    '''
    result=[0,0]
    if floatvalue:
        result[0]=random.uniform(LowValue,HighValue)
        result[1]=random.uniform(LowValue,HighValue)
    else:
        result[0]=random.randint(LowValue,HighValue)
        result[1]=random.randint(LowValue,HighValue)
    return result

def vector3D_random(floatvalue=False,LowValue=0,HighValue=10):
    '''
    Return a random 3D vector
    '''
    result=[0,0,0]
    if floatvalue:
        result[0]=random.uniform(LowValue,HighValue)
        result[1]=random.uniform(LowValue,HighValue)
        result[2]=random.uniform(LowValue,HighValue)
    else:
        result[0]=random.randint(LowValue,HighValue)
        result[1]=random.randint(LowValue,HighValue)
        result[2]=random.randint(LowValue,HighValue)
    return result

def vector2D_add(aArray,bArray):
    '''
    Add two 2D vectors using python core
    '''
    result=[0,0]
    for i in range(2):
        result[i]=aArray[i]+bArray[i]
    return result

def vector3D_add(aArray,bArray):
    '''
    Add two 3D vectors using python core`
    '''
    result=[0,0,0]
    for i in range(3):
        result[i]=aArray[i]+bArray[i]
    return result

def vector2D_subtract(aArray,bArray):
    '''
    Subtract two 2D vectors using python core
    '''
    result=[0,0]
    for i in range(2):
        result[i]=aArray[i]-bArray[i]
    return result

def vector3D_subtract(aArray,bArray):
    '''
    Subtract two 3D vectors using python core`
    '''
    result=[0,0,0]
    for i in range(3):
        result[i]=aArray[i]-bArray[i]
    return result
