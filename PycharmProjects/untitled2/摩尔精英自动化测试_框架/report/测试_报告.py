#! /usr/bin/env python
#! -*- coding:utf-8 -*-



from 摩尔精英自动化测试_框架.test_摩尔.测试_用例 import 测试_用例_1
import unittest
import HTMLTestRunne
import HTMLTestRunnertest
import time






def 报告(aa):
    suit = unittest.TestSuite()
    for a in aa:
        discover = unittest.defaultTestLoader.discover('..\hao_test', pattern='{}.py'.format(a.strip()))
        suit.addTest(discover)

    now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
    with open(r'C:\Users\fxs\PycharmProjects\untitled2\框架\report\all2.html', 'wb') as f:
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='fxs',
                                                   description='测试结果如下：',
                                                   title='摩尔精英_测试',
                                                   stream=f)
        runner.run(suit)
        f.close()

