#! /usr/bin/env python
#! -*- coding:utf-8 -*-






import xlrd

def duqu():
    shuju1 = []
    f = xlrd.open_workbook(r'C:\Users\fxs\PycharmProjects\untitled2\web自动化\data\web.xls')
    # sheet = f.nsheets
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1, num):
        oo = sheet.row_values(i)
        shuju1.append(oo)
    # pp = sheet.col_values(0)
    return shuju1

print(duqu())



def duqu1():
    shuju2 = []
    f = xlrd.open_workbook(r'C:\Users\fxs\PycharmProjects\untitled2\web自动化\data\kkk.xls')
    # sheet = f.nsheets
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1, num):
        oo = sheet.row_values(i)
        shuju2.append(oo)
    # pp = sheet.col_values(0)
    return shuju2

print(duqu1())


