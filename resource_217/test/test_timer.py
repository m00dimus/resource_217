 #// ------------------------------------
#// Title: test_timer.py
#// Description: Test examples for
#//    resource_timer.py
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20180130 (python 3.4.3)
#// ------------------------------------

import sys
sys.path.append("../")

import random
import time
import resource_timer as test

def wait(ms):
    time.sleep(ms/1000)

def main():
    print('Test examples for resource_timer.py')

    print('\n')
    print('Test #1 - Create a timer')
    object=test.timer()

    print('Wait 500ms\n')
    wait(500)

    print('\n')
    print('Test #2 - Show current timer showstatus')
    object.showstatus()

    print('Wait 500ms\n')
    wait(500)

    print('\n')
    print('Test #3 - Show timer results')
    object.results()

    print('\n')
    print('Test #4 - Restart timer and show status in a loop')
    object.start()
    for i in range(10):
        print('Wait 1000ms\n')
        wait(1000)
        object.showstatus()
    print('\n')
    print('Show timer final results')
    object.results()

if __name__ == '__main__':
    main()
