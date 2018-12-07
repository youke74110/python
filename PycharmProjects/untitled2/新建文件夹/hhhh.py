

import os
import xlwt
import xlrd
# from xlutils.copy import copyt
import pymysql
import re
import requests
import time
import paramiko
import time

# def xiaoshuo(a):
#     url = 'http://www.biquge.com.tw/0_270/{}.html'.format(a)
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
#     res = requests.get(url = url,headers = head)
#     html = res.content.decode('gbk')
#     # print(html)
#
#     patt = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S)
#     items = patt.findall(html)
#     # print(items)
#
#     for i in items:
#         with open('C:\\Users\\fxs\\Desktop\\鬼吹灯.txt','a',encoding='utf-8') as f:
#             f.write(i+'\n')
# for j in range(208453,211283):
#     xiaoshuo(j)









# server 端
import socket
## TCP
# 创建一个socket ,封装协议（第一个是ipv4协议，第二个是tcp协议）
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 绑定ip和端口号 bind接受的参数是元组
# host = ('192.168.0.55',54321)
# s.bind(host)
# # 监听 数字指的是：最大等待数
# s.listen(3)
# while True:
#     #接受请求
#     a,b = s.accept()      # 第一个结果a：是客户端的链接信息  # 第二个结果b：是客户端的IP地址和端口号
#     #接收数据
#     msg = a.recv(1024)      #1024代表的是 ：每次接收的最大字节数
#     print(msg.decode('utf-8'))
#     #发送响应
#     reg = 'nice'
#     a.send(reg.encode('utf-8'))





## UDP
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
# host = ('192.168.0.55',54321)
# s.bind(host)
# while True:
#     a,b = s.recvfrom(1024)  # 接收数据 第一个变量：客户端发送的请求数据，第二个变量：是客户端的ip地址和端口号
#     print(a.decode('utf-8'))
#     print(b)
#     #发送响应数据
#     msg = 'hello'
#     s.sendto(msg.encode('utf-8'),b)



























