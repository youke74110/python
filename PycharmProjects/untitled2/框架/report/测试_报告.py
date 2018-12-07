#! /usr/bin/env python
#! -*- coding:utf-8 -*-






from 框架.hao_test.test_学校 import xuexiao1
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
    with open(r'C:\Users\fxs\PycharmProjects\untitled2\框架\report\all2.html', 'wb') as f:
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='fxs',
                                                   description='测试结果如下：',
                                                   title='好分数测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()



















# if __name__=='__main__':

    # 生成测试报告 创建一个测试套件
    # suit = unittest.TestSuite()
    #
    # suit.addTest(unittest.makeSuite(xuexiao1))
    # now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    # with open('all4.html','wb') as f:
    #     runner = HTMLTestRunnertest.HTMLTestRunner(tester='fxs',
    #                                                    description = '测试结果如下：',
    #                                                    title = '好分数测试报告',
    #                                                    stream = f)
    #     runner.run(suit)
    #     f.close()













# def baogao2():
#     suit = unittest.TestSuite()
#     disvover = unittest.defaultTestLoader.discover('..\hao_test', pattern='test*.py')
#     suit.addTest(disvover)
#     now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
#     with open('all3.html', 'wb') as f:
#         runner = HTMLTestRunnertest.HTMLTestRunner(tester='fxs',
#                                                    description='测试结果如下：',
#                                                    title='好分数测试报告',
#                                                    stream=f)
#         runner.run(suit)
#         f.close()