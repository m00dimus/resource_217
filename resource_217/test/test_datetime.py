#// ------------------------------------
#// Title: test_datetime.py
#// Description: Test examples for
#//    resource_datetime.py
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160116 (python 3.4.3)
#// ------------------------------------

import sys
sys.path.append("../")

import resource_datetime as test
import random

def main():
    print('Test examples for resource_datetime.py')

    print('\n')
    print('Show current timestamp in YYYY-MM-DD HH:MM:SS format')
    print(test.get_current_timestamp())

    print('\n')
    print('Show current date in YYYY-MM-DD format')
    print(test.get_current_date())

    print('\n')
    print('Show current time in HH:MM:SS format')
    print(test.get_current_time())

    print('\n')
    print('Show current formal date in DayName, MonthName DD, YYYY')
    print(test.get_current_formal_date())

    print('\n')
    currentdate=test.get_current_timestamp()
    print('Check if current timestamp is valid. - ' + currentdate)
    print(test.isvaliddate(currentdate))

    print('\n')
    testdate='2016-13-29 12:22:33'
    print('Check if timestamp is valid with large month. - ' + testdate)
    print(test.isvaliddate(testdate))

    print('\n')
    testdate='2016-11-32 12:22:33'
    print('Check if timestamp is valid with large day. - ' + testdate)
    print(test.isvaliddate(testdate))

    print('\n')
    testdate='2016-11-32 26:22:33'
    print('Check if timestamp is valid with large hour. - ' + testdate)
    print(test.isvaliddate(testdate))

    print('\n')
    testdate='2016-11-30 12:68:33'
    print('Check if timestamp is valid with large minute. - ' + testdate)
    print(test.isvaliddate(testdate))

    print('\n')
    testdate='2016-11-30 12:22:60'
    print('Check if timestamp is valid with large second. - ' + testdate)
    print(test.isvaliddate(testdate))

    print('\n')
    testdate='20161130_122233'
    print('Check if timestamp is valid with unexpected format - ' + testdate)
    print(test.isvaliddate(testdate))

    print('\n')
    testdate='20161130_122233'
    testformat='%Y%m%d_%H%M%S'
    print('Check if timestamp is valid with custom format - ' + testdate + ',' + testformat)
    print(test.isvaliddate(testdate,testformat))

    print('\n')
    testdate='20161131_122233'
    testformat='%Y%m%d_%H%M%S'
    print('Check if timestamp is valid with large day using custom format - ' + testdate + ',' + testformat)
    print(test.isvaliddate(testdate,testformat))

    print('\n')
    testdate='20161330_122233'
    testformat='%Y%m%d_%H%M%S'
    print('Check if timestamp is valid with large month using custom format - ' + testdate + ',' + testformat)
    print(test.isvaliddate(testdate,testformat))

    print('\n')
    currentdate=test.get_current_timestamp()
    print('Get current timestamp with no offset. - ' + currentdate)
    print(test.gettimestampoffset(currentdate))

    print('\n')
    currentdate=test.get_current_timestamp()
    print('Get current timestamp with 10 second offset. - ' + currentdate)
    print(test.gettimestampoffset(currentdate,seconds=10))

    print('\n')
    currentdate=test.get_current_timestamp()
    print('Get current timestamp with 10 second negative offset. - ' + currentdate)
    print(test.gettimestampoffset(currentdate,seconds=-10))

    print('\n')
    currentdate=test.get_current_timestamp()
    randval=random.randint(0,60)
    print('Get current timestamp with random (' + str(randval) + ') second offset. - ' + currentdate)
    print(test.gettimestampoffset(currentdate,seconds=randval))

    print('\n')
    currentdate=test.get_current_timestamp()
    print('Get current timestamp with 1 day offset. - ' + currentdate)
    print(test.gettimestampoffset(currentdate,days=1))

    print('\n')
    currentdate=test.get_current_timestamp()
    print('Get current timestamp with 1.5 day offset. - ' + currentdate)
    print(test.gettimestampoffset(currentdate,days=1.5))

    print('\n')
    currentdate=test.get_current_timestamp()
    print('Get current timestamp with 1 day negative offset. - ' + currentdate)
    print(test.gettimestampoffset(currentdate,days=-1))

    print('\n')
    currentdate=test.get_current_timestamp()
    randval=random.randint(0,60)
    print('Get current timestamp with random (' + str(randval) + ') day offset. - ' + currentdate)
    print(test.gettimestampoffset(currentdate,days=randval))

    print('\n')
    currentdate=test.get_current_timestamp()
    print('Get current timestamp with 1 day plus 1 hour offset. - ' + currentdate)
    print(test.gettimestampoffset(currentdate,days=1,seconds=3600))

    startdate='2016-01-01 12:00:00'
    enddate='2016-01-01 12:00:01'
    ipass=1
    for enddate in ['2016-01-01 12:00:30','2016-01-01 12:05:00','2016-01-01 18:00:00','2016-01-03 12:00:00','2016-02-01 18:00:00','2067-02-01 12:00:00']:
        print('DateDiff Loop - Pass #' + str(ipass))
        print('Get difference between two dates in seconds. - ' + startdate + ' and ' + enddate)
        print(test.datediff(startdate,enddate,seconds=True))

        print('Get difference between two dates in minutes. - ' + startdate + ' and ' + enddate)
        print(test.datediff(startdate,enddate,minutes=True))

        print('Get difference between two dates in hours. - ' + startdate + ' and ' + enddate)
        print(test.datediff(startdate,enddate,hours=True))

        print('Get difference between two dates in days. - ' + startdate + ' and ' + enddate)
        print(test.datediff(startdate,enddate,days=True))
        print('\n')
        ipass=ipass+1

    startdate='2015-01-01 00:00:00'
    enddate='2016-01-01 00:00:00'
    print('Get difference between two dates (standard year) in days. - ' + startdate + ' and ' + enddate)
    print(test.datediff(startdate,enddate,days=True))

    print('\n')
    startdate='2016-01-01 00:00:00'
    enddate='2017-01-01 00:00:00'
    print('Get difference between two dates (leap year) in days. - ' + startdate + ' and ' + enddate)
    print(test.datediff(startdate,enddate,days=True))

if __name__ == '__main__':
    main()
