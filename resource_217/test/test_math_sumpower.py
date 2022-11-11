#// ------------------------------------
#// Title: test_math.py
#// Description: Test examples for
#//    resource_math.py
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160115 (python 3.4.3)
#// ------------------------------------

import sys
sys.path.append("../")

import resource_math as test
import resource_datetime as dt
import random
import time

def sim10k(n,k):
    j=0
    m=1e5

    start = time.time()
    while j<m:
        result=test.sumpowers(n,k)
        j=j+1
    end = time.time()
    print(result)
    print(end - start)

def main():
    starttime = time.time()
    print('Performing 10K simulations.')
    n=100

    k=2
    print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    sim10k(n,k)

    k=3
    print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    sim10k(n,k)

    k=4
    print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    sim10k(n,k)

    k=5
    print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    sim10k(n,k)

    k=6
    print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    sim10k(n,k)

    k=7
    print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    sim10k(n,k)

    k=8
    #print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    #sim10k(n,k)

    k=9
    #print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    #sim10k(n,k)

    k=10
    #print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    #sim10k(n,k)

    k=11
    #print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    #sim10k(n,k)

    k=12
    #print('Test sum powers for sum n=' + str(n) + ' x^' + str(k))
    #sim10k(n,k)

    endtime=time.time()
    elapsedtime = dt.datediff1(starttime,endtime,seconds=True)

    print(elapsedtime)
if __name__ == '__main__':
    main()
