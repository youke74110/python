# /bin/usr/env python
# -*- conding:utf-8 -*-


import re
import requests


# url = 'http://pic.netbian.com/4kdongman/index_4.html'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# reponse = requests.get(url=url,headers=head)
# html = reponse.content.decode('gbk')
# # # # print(html)
#
# patt = re.compile('<img src=(.*?) alt')
# items = patt.findall(html)
# # # # print(items)
# for i in items:
#     pp = i.replace('"','')
#     pp = 'http:/'+pp
#     print(pp)
#     tupian = requests.get(url=url)
#     tupian = requests.get(pp)
#     res1 = tupian.content.decode('gbk')
#     print(res1)
#     with open('{}.jpg'.format(i),'wb') as f:
#         f.write(res1)



# url = 'http://uploads/allimg/181018/153332-1539848012ed6d.jpg'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# reponse = requests.get(url = url)
# html = reponse.content.decode('gbk')
# print(html)
import xlwt
import xlrd




# url = 'https://www.pixiv.net/search.php?word=%E6%9E%AA%E7%A5%9E%E7%BA%AA&order=date_d&p=2'

# repon = requests.get(url = url,headers = head)
# html = repon.content.decode('utf-8')
# print(html)


# url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=20&type=T'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# repon = requests.get(url = url,headers = head)
# html = repon.content.decode('utf-8')
# # print(html)
# aaa = xlwt.Workbook(encoding='utf-8')
# she = aaa.add_sheet('豆瓣')
# she.write(0,0,'书名')
# she.write(0,1,'简介')
# patt = re.compile('<div class="info">(.*?)<div class="ft">',re.S)
# ite = patt.findall(html)
# for i in ite:
#     # patt1 = re.compile('title="(.*?)"',i,re.S)
#     shum = re.findall(r'title="(.*?)"',i,re.S)
#     miaos = re.findall(r'<p>(.*?)</p>',i,re.S)

    # for n in shum:
    #     print(n)
        # she.write(n + 1, 0, m)



    # for f,g in enumerate(miaos):
    #     she.write(f+1,1,g)

# aaa.save('qqq.xls')


#     print(shum)
#     print(miaos)
# print(ite)










import requests
import re

# class zhua(object):
#     def qing(self,xxx):
#         url = 'https://www.doutula.com/article/list/?page={}'.format(xxx)
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
#         response = requests.get(url = url,headers=head)
#         html = response.content.decode('UTF-8')
#         return html
#
#     def g(self,ttt):
#         patt = re.compile(r'https://www.doutula.com/article/detail/[0-9]{7}')
#         items = patt.findall(ttt)
#         return items
#
#
# aaa = zhua()
# mm = aaa.qing(10)
# vv = aaa.g(mm)
# print(vv)
#
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# hh =0
# for i in vv:
#     respons = requests.get(url=i,headers=head)
#     html1 = respons.content.decode('UTF-8')
#     patt1 = re.compile(r'<img src="https://ws(.*?) alt')
#     items1 = patt1.findall(html1)
#     # break
#     print(items1)
#
#     for i,j in enumerate(items1):
#         j = j.replace('"','')
#         j = 'https://ws'+j
#         tupian = requests.get(url=j,headers=head)
#         # print(j)
#         res1 = tupian.content
#         # print(res1)
#         with open('{}.jpg'.format(i),'wb') as f:
#                 # with open('{}.gif'.format(i),'ab') as f:
#             f.write(res1)
#         break




# url = 'http://www.7160.com/cosplay/43998/index_2.html'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# reponse = requests.get(url = url,headers = head)
# html = reponse.content.decode('gbk')
# # print(html)
#
# patt = re.compile(r'<img src=(.*?) alt',re.S)
# items = patt.findall(html)
# # print(items)
# for i in items:
#     patt1 = re.compile(r'<img srchttp://www.7160.com/templets/new7160/(.*?) alt',re.S)
#     items1 = patt1.findall(i)
#     print(items1)




# for i,j in enumerate(items):
#     j = j.replace('"','')
#     tupian = requests.get(j)
#
#     res1 = tupian.content
#     with open('{}.jpg'.format(i),'wb') as f:
#         f.write(res1)





aa = int(input('请输入数字：'))
url = 'http://www.7160.com/xiaohua/list_6_{}.html'.format(aa)
reponse = requests.get(url = url)
html = reponse.content.decode('gbk')
# print(html)
patt = re.compile(r'<img src="http://(.*?) alt',re.S)
items = patt.findall(html)
# print(items)
for i,j in enumerate(items):
    j=j.replace('"','')
    j = 'http://'+j
    tupian = requests.get(j)
    res1 = tupian.content
    with open('C:\\Users\\fxs\\Desktop\\fxs123\\11\\{}.jpg'.format(i),'wb') as f:
        f.write(res1)



























































































