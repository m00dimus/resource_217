#// ------------------------------------
#// Title: test_string.py
#// Description: Test examples for
#//    resource_string.py
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160115 (python 3.4.3)
#// ------------------------------------

import resource_string as test

def main(): 
    '''
    Test string module
    '''
    print('Test examples for resource_string.py')

    s_lower=['a','b','c','d','e','f','g','h',
             'i','j','k','l','m','n','o','p',
             'q','r','s','t','u','v','w','x','y','z']
    print('Test all lower consonants')
    for s in s_lower:
        if test.isconsonant(s):
            print(s + ' is a consonant')
        else:
            pass
            #print(s + ' is not a consonant')
            
    s_upper=['A','B','C','D','E','F','G','H',
             'I','J','K','L','M','N','O','P',
             'Q','R','S','T','U','V','W','X','Y','Z']

    print('\n') 
    print('Test all upper consonants')
    for s in s_upper:
        if test.isconsonant(s):
            print(s + ' is a consonant')
        else:
            pass
            #print(s + ' is not a consonant')

    print('\n') 
    s_lower=['a','b','c','d','e','f','g','h',
             'i','j','k','l','m','n','o','p',
             'q','r','s','t','u','v','w','x','y','z']
    print('Test all lower vowels')
    for s in s_lower:
        if test.isvowel(s):
            print(s + ' is a vowel')
        else:
            pass
            #print(s + ' is not a vowel')
            
    s_upper=['A','B','C','D','E','F','G','H',
             'I','J','K','L','M','N','O','P',
             'Q','R','S','T','U','V','W','X','Y','Z']

    print('\n') 
    print('Test all upper vowels')
    for s in s_upper:
        if test.isvowel(s):
            print(s + ' is a vowel')
        else:
            pass
            #print(s + ' is not a vowel')

    s_testset=['1',1,3.14,'!','abc',(1,2,'a')]

    print('\n') 
    print('Test non alphabet characters')
    for s in s_testset:
        if test.isconsonant(s):
            print(str(s) + ' is a consonant')
        else:
            print(str(s) + ' is not a consonant')

        if test.isvowel(s):
            print(str(s) + ' is a vowel')
        else:
            print(str(s) + ' is not a vowel')



if __name__ == '__main__':
    main()
