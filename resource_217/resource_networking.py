import random

#// avoid broadcast IPv4s

def GetRandomIPv4(ipaddrlower='',ipaddrupper=''):
    '''
    Return random IPv4 address in standard format. Includes non routeable addresses.
    '''
    randstep=1

    if ipaddrlower:
        numlower = IPv4toNum(ipaddrlower)
    else:
        numlower = IPv4toNum('1.1.1.1')
    if ipaddrupper:
        numupper = IPv4toNum(ipaddrupper)
    else:
        numupper = IPv4toNum('255.255.255.254')
    
    numipaddr = random.randrange(numlower,numupper,randstep)
    ipaddr = NumToIPv4(numipaddr)
    
    return ipaddr
    
def IsValidIPv4(ipaddr):
    '''
    Test if IPv4 is a valid numeric address
    '''
    try:
        ipv4 = ipaddr.split('.')
        for octet in ipv4:
            if int(octet) in range(1,256):
                pass
            else:
                return False
        return True
    except:
        return False

def IsValidIPv4Num(ipnumber):
    '''
    Test if number representation of IPv4 addres is a valid
    '''
    try:
        #// valid between 1.1.1.1 and 255.255.255.254
        if ipnumber > 16843009 and ipnumber < 4294967294:
            return True
        else:
            return False

    except:
        return False    
def IPv4toNum(ipaddr):
    '''
    Convert standard format IPv4 address to numeric representation
    '''
    if IsValidIPv4(ipaddr):
        ipv4 = ipaddr.split('.')
    else:
        return 0
        
    a = abs(int(ipv4[0])) * 2**24 #// 16777216
    b = abs(int(ipv4[1])) * 2**16 #// 65536
    c = abs(int(ipv4[2])) * 2**8 #// 256
    d = abs(int(ipv4[3]))
    
    number = a + b + c + d

    return number
    
def NumToIPv4(ipnumber):
    '''
    Convert numeric representation of IPv4 address to standard format
    '''
    if IsValidIPv4Num(ipnumber):
        pass
    else:
        return '0.0.0.0'
    a = int(ipnumber) // 2**24 #// first octet is 2^24
    b = int(ipnumber - a*2**24) // 2**16 #// second octet is 2^16
    c = int(ipnumber - a*2**24 - b*2**16) // 2**8 #// third octet is 2^8
    d = int(ipnumber - a*2**24 - b*2**16 - c*2**8) #// fourth octet is 2^1
    
    delim='.'
    ipaddr = str(a) + delim + str(b) + delim + str(c) + delim + str(d)

    return ipaddr

def IsRoutableIPv4(ipaddr):
    '''
    Test if IPv4 is a routeable address. See RF919 Section 7.
    '''
    num = IPv4toNum(ipaddr)
    #// Check 10.x.x.x - Class A
    if num >= 167837953 and num <=184549375:
        return False
    #// Check 172.16-31.x.x - Class B
    if num >= 2886729985 and num <=2887778303:
        return False    
    #// Check 192.168.x.x - Class C
    if num >= 3232235777 and num <=3232301055:
        return False    
    return True
    
def CountIPsInRange(ipaddrlower,ipaddrupper):
    '''
    Return count of IPs between two addresses
    '''
    count=0
    #// get number representation for lower bound
    ilower=IPv4toNum(ipaddrlower)
    #// get number representation for upper bound
    iupper=IPv4toNum(ipaddrupper)
    
    count= abs(iupper-ilower)
    return count

def GetRandomIPList(ipaddrlower,ipaddrupper,listlength=1):
    '''
    Return list of random IPs between two addresses
    '''
    iplist=[]
    #// get number representation for lower bound
    ilower=IPv4toNum(ipaddrlower)
    #// get number representation for upper bound
    iupper=IPv4toNum(ipaddrupper)

    #// test for swapped bounds on inputs
    if ilower > iupper:
        ilower = IPv4toNum(ipaddrupper)
        iupper=IPv4toNum(ipaddrlower)
        iplower = ipaddrupper
        ipupper = ipaddrlower
    else:
        iplower = ipaddrlower
        ipupper = ipaddrupper    
    while len(iplist) < listlength:
        #// get random IP adderss
        ipaddr = GetRandomIPv4(iplower,ipupper)
        #// check if ip address in within range
        if IPv4toNum(ipaddr) > ilower and IPv4toNum(ipaddr) < iupper:
            iplist.append(ipaddr) 
    return iplist

