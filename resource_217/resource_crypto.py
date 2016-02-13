#// ------------------------------------
#// Title: resource_crypto.py
#// Description: Simple crypto functions
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160115 (python 3.4.3)
#// ------------------------------------

import codecs

def rot13(t):
    if isinstance(t,str):
        c=codecs.encode(t, "rot_13")
    else:
        return ''
    return c

def rotn(t,n):
    '''
    Input a string and shift n charcters
    '''
    alpha_l='abcdefghijklmnpqrstuvwxyz'
    l_limit=122
    alpha_u='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    u_limit=89
    c=''
    p=[]
    if not isinstance(n,int) or n > 27:
        #// fail - n is not accepted
        return ''

    #// force positive?
    n=abs(n)
    
    #// test if string
    if isinstance(t,str):
        if t in alpha_l:
            if ord(t)+n < l_limit: 
                c=chr(ord(t)+n)
                print('Inside: ' + t + '('+str(ord(t))+')' +'-'+c +'('+str(ord(c)) + ')')
                return c
            #// wrap to the beginning of alphabet
            elif ord(t)+n > l_limit:
                v=ord(t)+n-26
                c=chr(v)
                print('Inside: ' + t + '('+str(ord(t))+')' +'-'+c +'('+str(ord(c)) + ')')
                return c                
            return c
        elif t in alpha_u:
            if ord(t)+n < u_limit: 
                c=chr(ord(t)+n)
                print('Inside: ' + t + '('+str(ord(t))+')' +'-'+c +'('+str(ord(c)) + ')')
                return c
            #// wrap to the beginning of alphabet
            elif ord(t)+n > u_limit:
                v=ord(t)+n-26
                c=chr(v)
                print('Inside: ' + t + '('+str(ord(t))+')' +'-'+c +'('+str(ord(c)) + ')')
                return c                
            return c             
    else:
        #// fail - t is not accepted
        return ''



##    #// test if string
##    if isinstance(t,str):
##        #// strings
##        if len(t) > 1:
##            for s in t:
##                if s.upper() in alpha:
##                    f=chr(ord(s)+13)
##                    print('Inside: ' + s + '('+str(ord(s))+')' +'-'+f +'('+str(ord(f)) + ')')
##                    p.append(f)
##            c=''.join(p)
##            return c
##        #// single character
##        elif len(t) == 1:
##            if t.upper() in alpha:
##                c=chr(ord(t)+13)
##                print('Inside: ' + t + '('+str(ord(t))+')' +'-'+c +'('+str(ord(c)) + ')')
##            return c
##    else:
##        return ''

alpha_l='abcdefghijklmnpqrstuvwxyz'
for c in alpha_l:
	print(c + '-' + str(ord(c)))
	
alpha_u='ABCDEFGHIJKLMNOPQRSTUVWXY'
for c in alpha_u:
	print(c + '-' + str(ord(c)))
	
print(rotn('a',1))
print(rotn('a',13))
print(rotn('z',1))
print(rotn('z',13))

print(rotn('A',1))
print(rotn('A',13))
print(rotn('Z',1))
print(rotn('Z',13))
#print(rot13('z'))
#print(rot13('1'))
#print(rot13(1))
#print(rot13('abc'))

#print(rot13('parkor'))

#print(rot13('A'))

#print(rot13('ABC'))

#print(rot13('parkor')) 
