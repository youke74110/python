# /usr/bin/env python
# -*- coding:utf-8 -*-


import unittest
from appium import webdriver
from time import sleep











#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end='\t')
#     print()

#





# 质数之和
# a = 0
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i % j == 0:
#             break
#     if j == i:
#         a = a+i
# print(a)






# 阶乘之和
# a = 1
# b = 0
# for i in range(1,6):
#     a = a*i
#     b = b+a
# print(b)



# 字符串回文
# a = 'asddsa'
# b = len(a)
# for i in range(b):
#     if a[i] != a[-i-1]:
#         print('不是回文字符串')
#         break
# else:
#     print('是回文字符串')






# 向左挪一位
# a = [1,2,2,3,'a','b']
# b = len(a)
# for i in range(1,b):
#     c = a[i]
#     a[i] = a[i-1]
#     a[i-1] = c
# print(a)





## 不用int将字符串变整数
# a = '123456'
# b = a[::-1]
# s = 0
# for i,j in enumerate(b):
#     for q in range(10):
#         if str(q) == j:
#             q = q*10**i
#             s = s+q
# print(s)




import requests
import re
import pymysql











# url = 'https://www.zhipin.com/c101010100-p100301/?page=1&ka=page-1'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
#
# res = requests.get(url = url,headers = head)
# html = res.content.decode('utf-8')
# # print(html)
#
# patt = re.compile(r'<div class="job-title">(.*?)</div>',re.S)
# items = patt.findall(html)
# a = items
# # print(a)
#
# patt1 = re.compile(r'<span class="red">(.*?)</span>',re.S)
# items1 = patt1.findall(html)
# b = items1
# # print(b)
#
# patt2 = re.compile(r'target="_blank">(.*?)</a></h3>')
# items2 = patt2.findall(html)
# c = items2
# # print(c)
#
#
# abc = pymysql.connect(host = '192.168.0.94',
#                       port = 3306,
#                       user = 'root',
#                       password = '654321',
#                       charset = 'utf8')
# aa = abc.cursor()
#
# # aa.execute('show databases;')
# aa.execute('use t_sc')
# # aa.execute('show tables')
#
# aa.execute('create table t_a(职位 char(50),薪资 char(50),公司 char(50))')
# # aa.execute('show tables')
#
# for i in a:
#     print(i)
# for j in b:
#     print(j)
# for k in c:
#     print(k)
#     with open('a.txt','a',encoding='utf-8') as f:
#          f.write('{},{},{}{}'.format(i,j,k,'\n'))
#
#
#
#
# with open('a.txt','r',encoding='utf-8') as k:
#     ee = k.readlines()
#     print(ee)
#     for t in ee:
#         q = t.replace('\n','').split(',')
#         aa.execute('insert into t_a values("{}","{}","{}");'.format(q[0],q[1],q[2]))
#
# aa.execute('select * from t_k;')
#
#
# print(aa.fetchall())



































##练习
##自动登录京东，搜索python，将python的第一个商品添加到购物车
# from selenium import webdriver
# from time import sleep
# class sj22(object):
#     def dddd(self):
#         self.jd=webdriver.Firefox()
#         self.jd.get('http://jd.com')
#         self.jd.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
#         sleep(2)
#         self.jd.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
#         sleep(2)
#         self.jd.find_element_by_xpath('//*[@id="loginname"]').send_keys('176379032')
#         self.jd.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('')
#         sleep(20)
#         self.jd.find_element_by_xpath('//*[@id="loginsubmit"]').click()
#         sleep(2)
#         self.jd.find_element_by_xpath('//*[@id="key"]').send_keys('python')
#         sleep(2)
#         self.jd.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
#         sleep(2)
#         self.jd.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[8]/a[2]').click()
#         sleep(2)
#     def aaaa(self):
#         all=self.jd.window_handles
#         self.jd.switch_to_window(all[0])
#         self.jd.find_element_by_xpath('//*[@id="settleup-2014"]/div[1]').click()
#         all1 = self.jd.window_handles
#         self.jd.switch_to_window(all1[1])
#         ab=self.jd.find_element_by_xpath('//*[@id="cart-floatbar"]/div/div/div/div[2]/div[4]/div[1]/div/div[2]/div/span[2]/em')
#         # print(ab.get_attribute('text'))
# sj22().dddd()
# sj22().aaaa()














class denglu(unittest.TestCase):

       def Deng(self):
              aaa = {'platformName':'Android',
                     'platformVersion':'5.1.1',
                     'deviceName':'emulator-5554',
                     'appPackage':'com.netease.cloudmusic',
                     'appActivity':'activity.LoadingActivity'}

              dr = webdriver.Remote('http://localhost:4723/wd/hub',aaa)


              print('立即体验')
              dr.find_element_by_id('com.netease.cloudmusic:id/mx').click()
              sleep(3)

              print('抽屉菜单')
              dr.find_element_by_id('com.netease.cloudmusic:id/py').click()
              sleep(2)

              print('立即登录')
              dr.find_element_by_id('com.netease.cloudmusic:id/abx').click()
              sleep(2)

              print('手机号登录')
              dr.find_element_by_id('com.netease.cloudmusic:id/pt').click()
              sleep(2)

              print('输入手机号')
              dr.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys('15137212732')
              sleep(2)

              print('输入密码')
              dr.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('fxs6802681')
              sleep(2)

              print('登录')
              dr.find_element_by_id('com.netease.cloudmusic:id/pt').click()
              sleep(2)


              aa = dr.find_element_by_id('com.netease.cloudmusic:id/ac2').text
              self.assertEqual(aa.text,'Atr丶逍遥')


if __name__=='__main__':
       unittest.main()









# print('每日推荐')
# dr.find_element_by_id('com.netease.cloudmusic:id/aaf').click()
# sleep(3)
#
# print('返回')
# dr.find_element_by_class_name('android.widget.ImageButton').click()
# sleep(2)
#
# print('歌单')
# dr.find_element_by_id('com.netease.cloudmusic:id/aaj').click()
# sleep(3)
#
# print('返回')
# dr.find_element_by_class_name('android.widget.ImageButton').click()
# sleep(2)
#
# print('搜索')
# dr.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()
# sleep(2)
#
# print('输入框')
# dr.find_element_by_id('com.netease.cloudmusic:id/search_src_text').send_keys('追梦赤子心')
# sleep(2)
#
# print('点击一下空白处')
# dr.find_element_by_id('com.netease.cloudmusic:id/a7v').click()
# sleep(2)













print('结束')
dr.quit()















