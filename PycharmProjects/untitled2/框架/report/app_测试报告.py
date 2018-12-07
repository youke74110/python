#! /usr/bin/env python
#! -*- coding:utf-8 -*-


from 框架.hao_test.test_某app import app_测试
import unittest
import HTMLTestRunne
import HTMLTestRunnertest
import time


def baogao1(aa):
    suit = unittest.TestSuite()
    for a in aa:
        discover = unittest.defaultTestLoader.discover('..\hao_test', pattern='{}.py'.format(a.strip()))
        suit.addTest(discover)

    now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
    with open(r'C:\Users\fxs\PycharmProjects\untitled2\框架\report\某app测试报告.html', 'wb') as f:
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='fxs',
                                                   description='测试结果如下：',
                                                   title='某app测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()



