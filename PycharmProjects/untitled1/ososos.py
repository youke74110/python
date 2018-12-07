# /usr/bin/env python
# -*- coding:utf -8 -*-
import random



import os

# a = os.popen('ping 192.168.0.1')
# print(a.read())
#
# print(os.getcwd())
#
#
# os.chdir('C:\\Users\\fxs\\PycharmProjects')   # 两个斜杠或者前面加r  ：为了让斜杠后面的字符不转义
#
# os.makedirs('C:\\Users\\fxs\\Desktop\\aaaa\\bbb\\ccc\\eee')   #递归创建
# os.removedirs('C:\\Users\\fxs\\Desktop\\aaa')
#
# os.remove('C:\\Users\\fxs\\Desktop\\a2.txt')
#
# print(os.listdir('C:\\Users\\fxs\\Desktop'))
#
# os.rename('osll.py','ososos.py')
# os.rename('f.txt','lol.py')
#
# print(os.path.split('C:\\Users\\fxs\\Desktop\\a2.txt'))
# print(os.path.splitext('C:\\Users\\fxs\\Desktop\\a2.txt'))
#
# print(os.path.isfile('c1.txt'))   # 判断是否为普通文件
# print(os.path.isdir())       # 判断是否为目录文件
# print(os.path.islink())     # 判断是否为链接文件




# for i in os.listdir():
#     if os.path.splitext(i)[1] == '.py':
#         print(i)



# print(os.path.isfile('C:\\Users\\fxs\\Desktop'))
# sun = 0
# sum = 0
# sun = 0
# sum = 0
#
# os.chdir('C:\\Users\\fxs\\Desktop')
# for i in os.listdir():
#     if os.path.isfile(i):
#         sun=sun+1
#     print(sun)
#
#     if os.path.isdir(i):
#         sum=sum+1
#     print(sum)



# a= [i for i in os.listdir() if os.path.isfile(i)]
# b= [i for i in os.listdir() if os.path.isdir(i)]
#
# print(len(a))
# print(len(b))


# import xlwt
# # 打开一个空白文件
# a = xlwt.Workbook(encoding='utf-8')
# # #添加一个标签页，括号中写标签页的名称
# sheet = a.add_sheet('python表格')
# # 写入数据
#       # 第一个数字代表多少行  第一行从0开始
#       # 第二个数字代表多少列  第一列从0开始
#       # 第三个字符串代表写入的内容
# sheet.write(0,0,'姓名')
# sheet.write(0,1,'年龄')
# sheet.write(0,2,'班级')
#
# # 保存
#
#
#
#
#
# for i in range(1,31):
#     sheet.write(i,0,'小明')
#     sheet.write(i,1,20)
#     sheet.write(i,2,1201)
# a.save('ttt.xls')


# b = ['小明',20,1201]
# for i in (b):
#     for j in range(30):









