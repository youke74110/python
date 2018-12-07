#! /usr/bin/env python
#! -*- coding:utf-8 -*-


import unittest

import time
from 框架.report import HTMLTestRunnertest


from 框架.report.测试_报告 import baogao1
from 框架.data.duqu_数据 import duqu2






class Test_run():
    def run_多个(self,i):
        baogao1(i)

    def run_all(self,i):
        baogao1(i)
if __name__=='__main__':
    run = Test_run()
    m = duqu2()
    if 'all' in m:
        b=['test*']
        run.run_all(b)
    else:
        run.run_多个(m)

























    # if __name__=='__main__':
    #     unittest.main()

    # # b = []
    # with open('abc.txt','r')as k:
    #     m = k.read()
    #     m = m.split('\n')
    #     # print(m)
    #     for i in m:
    #         with open(r'..\hao_test\{}.py'.format(i),'r',encoding='utf-8') as l:
    #             pp = l.read()
    #             print(pp)
    #             patt = re.compile(r'class (.*?)(unittest.TestCase):')
    #             ee = patt.findall()
    #










        # print(m)
        # if m in 'all':
        #     run.run_all()
        # else:
        #     run.run_多个()


##   1.所有的类加载到某个列表中





