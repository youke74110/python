#! /usr/bin/env python
#! -*- coding:utf-8 -*-

import requests
import re
import pymysql









# 1.

url = 'https://www.zhipin.com/c101010100-p100301/?page=1&ka=page-1'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

res = requests.get(url = url,headers = head)
html = res.content.decode('utf-8')
# print(html)

patt = re.compile(r'<div class="job-title">(.*?)</div>',re.S)
items = patt.findall(html)
a = items
# print(a)

patt1 = re.compile(r'<span class="red">(.*?)</span>',re.S)
items1 = patt1.findall(html)
b = items1
# print(b)

patt2 = re.compile(r'target="_blank">(.*?)</a></h3>')
items2 = patt2.findall(html)
c = items2
# print(c)


abc = pymysql.connect(host = '192.168.0.94',
                      port = 3306,
                      user = 'root',
                      password = '654321',
                      charset = 'utf8')
aa = abc.cursor()

# aa.execute('show databases;')
aa.execute('use t_sc')
# aa.execute('show tables')

aa.execute('create table t_a(职位 char(50),薪资 char(50),公司 char(50))')
# aa.execute('show tables')

for i in a:
    print(i)
for j in b:
    print(j)
for k in c:
    print(k)
    with open('a.txt','a',encoding='utf-8') as f:
         f.write('{},{},{}{}'.format(i,j,k,'\n'))




with open('a.txt','r',encoding='utf-8') as k:
    ee = k.readlines()
    print(ee)
    for t in ee:
        q = t.replace('\n','').split(',')
        aa.execute('insert into t_a values("{}","{}","{}");'.format(q[0],q[1],q[2]))

aa.execute('select * from t_k;')


print(aa.fetchall())







