#!/usr/bin/env python

import socket

SSDP_DICT = { 'ip_address' : '239.255.255.250',
              'port'       : 1900,
              'mx'         : 10,
              'st'         : 'ssdp:all' }

ssdp_request = '''M-SEARCH * HTTP/1.1
HOST: {ip_address}:{port}
MAN: "ssdp:discover"
MX: {mx}
ST: {st}

'''.replace('\n', '\r\n').format(**SSDP_DICT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(ssdp_request, (SSDP_DICT['ip_address'], SSDP_DICT['port']))
print(sock.getsockname())

sock.settimeout(5)# set 5 sec timeout
try:
    while True:
        print(sock.recv(1000))
except socket.timeout as e:
    pass
print('Done.')
