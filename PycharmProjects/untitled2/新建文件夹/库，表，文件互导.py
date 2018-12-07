#!/usr/bin/env python
# -*- coding:utf -8 -*-
import pymysql
import xlwt
import xlrd
# for xlutils.copy import copy









# abc = pymysql.connect(host = '192.168.0.103',
#                       port = 3306,
#                       user = 'root',
#                       password = '654321',
#                       charset = 'utf8')
# aaa = abc.cursor()
# aaa.execute('show databases;')
# aaa.execute('use xiao;')
# # aaa.execute('show tables;')
# aaa.execute('select * from tx;')
# b = aaa.fetchall()
# aaa.execute('desc tx')
# a = aaa.fetchall()
# for i in b:
#     print(i[0])
    # with open('xiao.txt','a',encoding='utf-8') as f:
    #     f.write(i[0]+'\n')
# for i in a:
#     print(i[0])
#     with open('xiao.txt','a',encoding='utf-8') as f:
#         f.write(i[0]+'\0')








# with open('C:\\Users\\fxs\\Desktop\\a.txt','r') as f:
#     a = f.readline()
#     b = a.split(',')
#     c = f.readlines()





















# f = xlrd.open_workbook('C:\\Users\\fxs\\Desktop\\tx.xlsx')
# sheet = f.nsheets
# sheet = f.sheets()[0]
# print(sheet.row_values(0))





























# 从txt文件导入数据库中
#
# import pymysql
#
# a=pymysql.connect(host='192.168.0.94',port=3306,
#                   user='root',password='654321',
#                   charset='utf8')
# b=a.cursor()
#
# b.execute('use xxx;')
# with open('b.txt','r',encoding='utf-8') as f:
#     aa=f.readline()
#     a=aa.split(',')
#     b.execute('create table bi({} char(20),{} char(20),{} char(30),{} char(20));'.format(a[0],a[1],a[2],a[3]))
#     aa = f.readlines()
#     for i in aa:
#         a=i.replace('\n','').split(",")
#         b.execute('insert into bi values("{}","{}","{}","{}");'.format(a[0], a[1], a[2], a[3]))
#
# b.execute('select * from bi;')
# x=b.fetchall()
# for j in x:
#     print(j)















# 从数据库导入txt中
#
# import pymysql
# a=pymysql.connect(host='192.168.0.94',port=3306,
#                   user='root',password='654321',
#                   charset='utf8')
#
# b=a.cursor()
# b.execute('show databases;')
# b.execute('use xiao;')
# # b.execute('insert into biao values("小花",12,"小班")')
# # b.execute('delete from biao where 姓名="小花";')
# # b.execute('update biao set 姓名="小花" where 年龄=30;')
# b.execute('desc biao_2;')
# c=b.fetchall()
# with open('b.txt','a',encoding='utf-8') as f:
#     f.write('{},{},{},{}\n'.format(c[0][0],c[1][0],c[2][0],c[3][0]))
#
#
# b.execute('select * from biao_2;')
# for i in b.fetchall():
#     with open('b.txt','a',encoding='utf-8') as f:
#         f.write('{},{},{},{}\n'.format(i[0],i[1],i[2],i[3]))
# print('over')















# 将数据库的文件写入到excel表格中
#
# import xlwt
# import pymysql
#
# a=pymysql.connect(host='192.168.0.94',port=3306,user='root',password='654321',charset='utf8')
# b=a.cursor()
#
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet_1')
#
# b.execute('use xiao;')
# b.execute('desc biao_2;')
# c=b.fetchall()
# for i in range(3):
#     sheet.write(0,i,'{}'.format(c[i][0]))
#
#
# b.execute('select * from biao_2;')
# c=b.fetchall()
# aa=1
# for i in c:
#     sheet.write(aa,0,'{}'.format(i[0]))
#     sheet.write(aa,1,'{}'.format(i[1]))
#     sheet.write(aa,2,'{}'.format(i[2]))
#     sheet.write(aa,3,'{}'.format(i[3]))
#     aa+=1
#
# f.save('test1.xls')
# print('over')















# txt文件中导入到表格
# import xlwt

# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet_1')
#
# with open(r'C:\Users\fxs\PycharmProjects\untitled2\a.txt','r',encoding='utf-8') as x:
#     a=x.read()
#     aa=a.split('\n')
#     bb=0
#     for i in aa:
#         i=i.split(',')
#         # print(i[])
#         sheet.write(bb,0,'{}'.format(i[0]))
#         sheet.write(bb,1,'{}'.format(i[1]))
#         sheet.write(bb,2,'{}'.format(i[2]))
#         sheet.write(bb,3,'{}'.format(i[3]))
#         bb+=1
# f.save('test.xls')
# print('over')















# 从excel到数据库
# import pymysql
# import xlrd
#
# aa=pymysql.connect(host='192.168.0.94',port=3306,user='root',password='654321',charset='utf8')
# bb=aa.cursor()
# bb.execute('use xiao')
#
# #
# a=xlrd.open_workbook(r'C:\Users\fxs\Desktop\tx.xls')
# sheet=a.nsheets         # 获取有多少个标签页
# sheet=a.sheets()[0]
# b=sheet.row_values(0)
# bb.execute('create table biao_2({} char(20),{} char(20),{} char(20),{} char(20));'.format(b[0],b[1],b[2],b[3]))
# b=sheet.nrows
# for i in range(1,b):
#     b=sheet.row_values(i)
#     bb.execute('insert into biao_2 values("{}","{}","{}","{}");'.format(b[0],b[1],b[2],b[3]))
# bb.execute('select * from biao_2;')
# cc=bb.fetchall()
# print(cc)















# 表格到txt
#
# a=xlrd.open_workbook(r'C:\Users\fxs\Desktop\tx.xls')
# sheet=a.sheet_by_name('Sheet1')
# b=sheet.row_values(0)
# with open('a.txt','w',encoding='utf-8') as f:
#     f.write('{},{},{},{}\n'.format(b[0],b[1],b[2],b[3]))
# b=sheet.nrows
# for i in range(1,b):
#     c=sheet.row_values(i)
#     with open('a.txt', 'a', encoding='utf-8') as f:
#         f.write('{},{},{},{}\n'.format(c[0], c[1], c[2], c[3]))









if __name__ == '__main__':



