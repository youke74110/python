#! /usr/bin/env python
#! -*- encoding:utf-8 -*-
import socket


soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

soc.connect(('192.168.0.27',54321))
aaa = 'lue'
soc.send(aaa.encode('utf-8'))
msg = soc.recv(1024)
print(msg.decode('utf-8'))









# soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host = ('192.168.0.27',54321)
# # while True:
# a = (host)
# reg = 'hi'
# soc.sendto(reg.encode('utf-8'),a)
# c = soc.recv(1024)
# print(c.decode('utf-8'))













