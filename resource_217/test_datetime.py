#// ------------------------------------
#// Title: test_datetime.py
#// Description: Test examples for
#//    resource_datetime.py
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160116 (python 3.4.3)
#// ------------------------------------

import resource_datetime as test

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
      
if __name__ == '__main__':
    main()
