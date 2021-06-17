import ipaddress, subprocess



myIpAddress = input('1.debian.pool.ntp.org')
myAdd = ipaddress.ip_interface(myIpAddress)
myNet = ipaddress.ip_network(myAdd, strict = True) # False lets you enter any ip address in the /24 ip address block.
for i in myNet:
    canPing = subprocess.call('ping /n 2 /w 1000 %s' % str(i))
    if canPing == 0:
        print('I can ping %s.' % str(i))
    if canPing == 1:
        print('%s is not responding' % str(i))
