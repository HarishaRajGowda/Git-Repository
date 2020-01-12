import ipaddress
subnet = ipaddress.IPv4Network('192.168.100.0/27');
for ipv4 in subnet.hosts():
    print(ipv4)

a = 100
b = 200
if a > b:
    print('{} is Greater than {}'.format(a,b))
else:
    print('{} is Greater than {}'.format(b,a))
