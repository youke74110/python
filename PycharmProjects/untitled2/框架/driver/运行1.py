#! /usr/bin/env python
#! -*- coding:utf-8 -*-



import unittest
from 框架.report import HTMLTestRunnertest
import time

from 框架.report.app_测试报告 import baogao1
from 框架.data.duqu1_数据 import duqu2





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









