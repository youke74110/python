#! /usr/bin/env python
#! -*- coding:utf-8 -*-



import xlrd


def duqu1():
    shuju1 = []
    f = xlrd.open_workbook(r'C:\Users\fxs\PycharmProjects\untitled2\框架\data\asd.xls')
    # sheet = f.nsheets
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1, num):
        oo = sheet.row_values(i)
        shuju1.append(oo)
    # pp = sheet.col_values(0)
    return shuju1

print(duqu1())


def duqu2():
    b = []
    with open(r'C:\Users\fxs\PycharmProjects\untitled2\框架\data\abc.txt','r')as k:
        m = k.readlines()
        for i in m:
            u = i.replace('\n','')
            b.append(u)

        return b


print(duqu2())
