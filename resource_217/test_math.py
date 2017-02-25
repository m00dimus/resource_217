#// ------------------------------------
#// Title: test_math.py
#// Description: Test examples for
#//    resource_math.py
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160115 (python 3.4.3)
#// ------------------------------------

import resource_math as test
import random

def main():
    print('Test examples for resource_math.py')

    #// Test isprime function
    i_testset=range(30)
    print('Test positive integers for primes')
    for i in i_testset:
        if test.isprime(i):
            print('Pass: ' + str(i) + ' is prime')

    print('\n')
    i_testset=range(-30,0)
    print('Test negative integers for primes')
    for i in i_testset:
        if test.isprime(i):
            print('Pass: ' + str(i) + ' is prime')

    print('\n')
    i_testset=random.random()
    print('Test random real for prime')
    if not test.isprime(i_testset):
        print('Fail: ' + str(i_testset) + ' is not prime')

    print('\n')
    i_testset=['a','abc','!','17',17,'2',2,(1,7,'a')]
    print('Test random inputs for primes')
    for i in i_testset:
        if test.isprime(i):
            print('Pass: ' + str(i) + ' is prime')
        else:
            print('Fail: ' + str(i) + ' is not prime')

    print('\n')
    #// Test iseven function
    i_testset=range(10)
    print('Test positive integers for evens')
    for i in i_testset:
        if test.iseven(i):
            print('Pass: ' + str(i) + ' is even')
        else:
            print('Fail: ' + str(i) + ' is not even')

    print('\n')
    i_testset=range(-10,0)
    print('Test negative integers for evens')
    for i in i_testset:
        if test.iseven(i):
            print('Pass: ' + str(i) + ' is even')
        else:
            print('Fail: ' + str(i) + ' is not even')

    print('\n')
    i_testset=random.random()
    print('Test random real for even')
    if not test.iseven(i_testset):
        print('Fail: ' + str(i_testset) + ' is not even')

    print('\n')
    i_testset=['a','abc','!','17',17,'2',2]
    print('Test random inputs for even')
    for i in i_testset:
        if test.iseven(i):
            print('Pass: ' + str(i) + ' is even')
        else:
            print('Fail: ' + str(i) + ' is not even')


    #// Test isodd function

    print('\n')
    i_testset=range(10)
    print('Test positive integers for odd')
    for i in i_testset:
        if test.isodd(i):
            print('Pass: ' + str(i) + ' is odd')
        else:
            print('Fail: ' + str(i) + ' is not odd')

    print('\n')
    i_testset=range(-10,0)
    print('Test negative integers for odd')
    for i in i_testset:
        if test.isodd(i):
            print('Pass: ' + str(i) + ' is odd')
        else:
            print('Fail: ' + str(i) + ' is not odd')

    print('\n')
    i_testset=random.random()
    print('Test random real for odd')
    if not test.isodd(i_testset):
        print('Fail: ' + str(i_testset) + ' is not odd')

    print('\n')
    i_testset=['a','abc','!','17',17,'2',2,(1,7,'a')]
    print('Test random inputs for even')
    for i in i_testset:
        if test.isodd(i):
            print('Pass: ' + str(i) + ' is odd')
        else:
            print('Fail: ' + str(i) + ' is not odd')

    #// Test vector functions

    print('\n')
    print('Test random 2D vector with default range')
    result=test.vector2D_random()
    print('Random 2D vector:',result)

    print('\n')
    print('Test random 3D vector with default range')
    result=test.vector3D_random()
    print('Random 3D vector:',result)

    print('\n')
    print('Test random 2D vector with default float range')
    result=test.vector2D_random(floatvalue=True)
    print('Random 2D vector:',result)

    print('\n')
    print('Test random 3D vector with default float range')
    result=test.vector3D_random(floatvalue=True)
    print('Random 3D vector:',result)

    print('\n')
    print('Test random 2D vector with specific range (0,2)')
    result=test.vector2D_random(LowValue=0,HighValue=2)
    print('Random 2D vector:',result)

    print('\n')
    print('Test random 3D vector with specific range (0,2)')
    result=test.vector3D_random(LowValue=0,HighValue=2)
    print('Random 3D vector:',result)

    print('\n')
    print('Test random 2D vector with specific float range (0,2)')
    result=test.vector2D_random(floatvalue=True,LowValue=0,HighValue=2)
    print('Random 2D vector:',result)

    print('\n')
    print('Test random 3D vector with specific float range (0,2)')
    result=test.vector3D_random(floatvalue=True,LowValue=0,HighValue=2)
    print('Random 3D vector:',result)

    #// Test vector magnitudes

    print('\n')
    print('Test random 2D vector magnitude from origin')
    aArray=[0,0]
    bArray=test.vector2D_random(LowValue=-5,HighValue=5)
    result=test.vector2D_magnitude(aArray,bArray)
    print('Random 2D vector magnitude:' + str(aArray) + ',' + str(bArray) + '=',result)

    print('\n')
    print('Test random 2D vector magnitude between two points')
    aArray=test.vector2D_random(LowValue=-5,HighValue=5)
    bArray=test.vector2D_random(LowValue=-5,HighValue=5)
    result=test.vector2D_magnitude(aArray,bArray)
    print('Random 2D vector magntude:' + str(aArray) + ',' + str(bArray) + '=',result)

    print('\n')
    print('Test random 2D vector magnitude from origin to float point')
    aArray=test.vector2D_random(floatvalue=True,LowValue=-5,HighValue=5)
    bArray=test.vector2D_random(floatvalue=True,LowValue=-5,HighValue=5)
    result=test.vector2D_magnitude(aArray,bArray)
    print('Random 2D vector magnitude:' + str(aArray) + ',' + str(bArray) + '=',result)

    print('\n')
    print('Test random 2D vector magnitude between two float points')
    aArray=test.vector2D_random(floatvalue=True,LowValue=-5,HighValue=5)
    bArray=test.vector2D_random(floatvalue=True,LowValue=-5,HighValue=5)
    result=test.vector2D_magnitude(aArray,bArray)
    print('Random 2D vector magnitude:' + str(aArray) + ',' + str(bArray) + '=',result)

    print('\n')
    print('Test random 3D vector magnitude from origin')
    aArray=[0,0,0]
    bArray=test.vector3D_random(LowValue=-5,HighValue=5)
    result=test.vector3D_magnitude(aArray,bArray)
    print('Random 3D vector magnitude:' + str(aArray) + ',' + str(bArray) + '=',result)

    print('\n')
    print('Test random 3D vector magnitude between two points')
    aArray=test.vector3D_random(LowValue=-5,HighValue=5)
    bArray=test.vector3D_random(LowValue=-5,HighValue=5)
    result=test.vector3D_magnitude(aArray,bArray)
    print('Random 3D vector magnitude:' + str(aArray) + ',' + str(bArray) + '=',result)

    print('\n')
    print('Test random 3D vector magnitude from origin to float point')
    aArray=test.vector3D_random(floatvalue=True,LowValue=-5,HighValue=5)
    bArray=test.vector3D_random(floatvalue=True,LowValue=-5,HighValue=5)
    result=test.vector3D_magnitude(aArray,bArray)
    print('Random 3D vector magnitude:' + str(aArray) + ',' + str(bArray) + '=',result)

    print('\n')
    print('Test random 3D vector magnitude between two float points')
    aArray=test.vector3D_random(floatvalue=True,LowValue=-5,HighValue=5)
    bArray=test.vector3D_random(floatvalue=True,LowValue=-5,HighValue=5)
    result=test.vector3D_magnitude(aArray,bArray)
    print('Random 3D vector magnitude:' + str(aArray) + ',' + str(bArray) + '=',result)

    #// test vector operations

    print('\n')
    print('Test 2D vector addition')
    a=[1,1]
    b=[2,3]
    result=test.vector2D_add(a,b)
    print(a,'+',b,'=',result)

    print('\n')
    print('Test 3D vector addition')
    a=[1,1,1]
    b=[3,4,5]
    result=test.vector3D_add(a,b)
    print(a,'+',b,'=',result)

    print('\n')
    print('Test 2D vector subtraction')
    a=[1,1]
    b=[2,3]
    result=test.vector2D_subtract(a,b)
    print(a,'-',b,'=',result)

    print('\n')
    print('Test 3D vector subtraction')
    a=[1,1,1]
    b=[3,4,5]
    result=test.vector3D_subtract(a,b)
    print(a,'-',b,'=',result)


if __name__ == '__main__':
    main()
