#// ------------------------------------
#// Title: test_networking.py
#// Description: Test examples for
#//    resource_networking.py
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.1-20160207 (python 3.4.3)
#// ------------------------------------

import resource_networking as test


def main(): 
    '''
    Test networking module
    '''
    print()
    print('Test Class C Network')
    ipaddrange=['9.255.255.255','10.10.1.1','10.255.255.255','11.1.1.1']
    for ipaddr in ipaddrange:
        if test.IsRoutableIPv4(ipaddr):
            print('Routable - ' + ipaddr)
        else:
            print('Not Routable - ' + ipaddr)
            
    print()
    print('Test Class B Network')
    ipaddrange=['172.15.255.255','172.16.1.1','172.31.255.255','172.32.1.1']
    for ipaddr in ipaddrange:
        if test.IsRoutableIPv4(ipaddr):
            print('Routable - ' + ipaddr)
        else:
            print('Not Routable - ' + ipaddr)
            
    
    print()
    print('Test Class C Network')
    ipaddrange=['192.167.255.255','192.168.1.1','192.168.255.255','192.169.1.1']
    for ipaddr in ipaddrange:
        if test.IsRoutableIPv4(ipaddr):
            print('Routable - ' + ipaddr)
        else:
            print('Not Routable - ' + ipaddr)
    

    print()
    print('Test Routable Random IPs')
    for i in range(10):
        ipaddr=test.GetRandomIPv4()
        if test.IsRoutableIPv4(ipaddr):
            print('Routable - ' + ipaddr)
        else:
            print('Not Routable - ' + ipaddr)

    print()
    print('Test Get List of Random IPs')
    iplower='7.1.1.1'
    ipupper='10.168.17.255'
    numberlist=15
    print('Getting ' + str(numberlist) + ' random IPs between ' + iplower + ' and ' + ipupper)
    iplist = test.GetRandomIPList(iplower,ipupper,numberlist)
    print(iplist)

    print()
    print('Getting default random IP between ' + iplower + ' and ' + ipupper)
    iplist = test.GetRandomIPList(iplower,ipupper)
    print(iplist)

    print()    
    print('Test swapped upper and lower inputs')
    print('Getting ' + str(numberlist) + ' random IPs between ' + ipupper + ' and ' + iplower)
    iplist = test.GetRandomIPList(ipupper,iplower,numberlist)
    print(iplist)

    print()
    print('Test Routable List of IPs')

    ipaddrange=['200.255.255.255','196.0.0.0','192.168.255.255','192.169.1.1']
    for ipaddr in ipaddrange:
        if test.IsRoutableIPv4(ipaddr):
            print('Routable - ' + ipaddr)
        else:
            print('Not Routable - ' + ipaddr)
    
    print()
    print('Test Count IPs in range')
    iplower='10.168.1.10'
    ipupper='10.168.1.25'
    num=test.CountIPsInRange(iplower,ipupper)
    print('There are ' + str(num) + ' between ' + iplower + ' and ' + ipupper)
    
    iplower='10.168.1.1'
    ipupper='10.168.2.255'
    num=test.CountIPsInRange(iplower,ipupper)
    print('There are ' + str(num) + ' between ' + iplower + ' and ' + ipupper)
    
    iplower='168.161.1.1'
    ipupper='170.163.255.255'
    num=test.CountIPsInRange(iplower,ipupper)
    print('There are ' + str(num) + ' between ' + iplower + ' and ' + ipupper)

    print('Test Count IPs in range')
    iplower='10.42.1.1'
    ipupper='10.42.255.254'
    num=test.CountIPsInRange(iplower,ipupper)
    print('There are ' + str(num) + ' between ' + iplower + ' and ' + ipupper)

  
    print()
    print('Test swapped upper and lower inputs')
    num=test.CountIPsInRange(ipupper,iplower)
    print('There are ' + str(num) + ' between ' + iplower + ' and ' + ipupper)
    
    print()
    print('Test malformed inputs')
    stripv4='aaa.bbb.ccc.ddd'
    print('Test value is :"' + stripv4 + '"')
    print('Test strings for IPv4toNum')
    print(test.IPv4toNum(stripv4))
    
    print('Test strings for NumToIPv4')
    print(test.NumToIPv4('aaa.bbb.ccc.ddd'))
    


if __name__ == '__main__':
    main()
