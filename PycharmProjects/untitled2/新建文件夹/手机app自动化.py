#! /usr/bin/env python
#! -*- coding:utf-8 -*-


# import unittest
from appium import webdriver
import time
# import unittest
# import HTMLTestRunne
# import HTMLTestRunnertest


##启动设备，连接设备
desired_caps = {'platformName':'Android',
                # 'platformVersion':'5.0',
                'deviceName':'emulator-5554',
                'appPackage':'com.netease.cloudmusic',
                'appActivity':'activity.LoadingActivity'}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

print('立即体验')
driver.find_element_by_id('com.netease.cloudmusic:id/mx').click()
time.sleep(3)

print('抽屉菜单')
driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
time.sleep(2)

print('立即登录')
driver.find_element_by_id('com.netease.cloudmusic:id/abx').click()
time.sleep(2)

print('手机号登录')
driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
time.sleep(2)

print('输入手机号')
driver.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys('15137212732')
time.sleep(2)

print('输入密码')
driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('fxs6802681')
time.sleep(2)

print('登录')
driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
time.sleep(2)

## 断言

print('点击抽屉菜单')
driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
time.sleep(2)


print('用户名')
a = driver.find_element_by_id('com.netease.cloudmusic:id/ac2').text
aa = 'Atr丶逍遥'
if a == aa:
    print('登录成功')







# suit = unittest.TestSuite()
# for a in aa:
#     discover = unittest.defaultTestLoader.discover('..\hao_test', pattern='{}.py'.format(a.strip(a)))
#     suit.addTest(discover)

# now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
# with open(r'C:\Users\fxs\PycharmProjects\untitled2\新建文件夹\all2.html', 'wb') as f:
#     runner = HTMLTestRunnertest.HTMLTestRunner(tester='fxs',
#                                                 description='测试结果如下：',
#                                                 title='好分数测试报告',
#                                                 stream=f)
#     runner.run(suit)
#     f.close()







print('结束')
driver.quit()




















