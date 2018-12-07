#! /usr/bin/env python
#! -*- coding:utf-8 -*-


import unittest
from 框架1.config.某app_接口 import app_接口
from 框架1.data.duqu1_数据 import duqu1


# shuju = duqu1()
# print(shuju)

class app_测试(unittest.TestCase):
    tes_app = app_接口.app_接口1
    shuju = duqu1()
    # print(shuju)
    def test_1(self):

        lll = self.tes_app(str(int(self.shuju[0][0])))
        self.assertEqual(lll['code'],str(int(self.shuju[0][2])))
        self.assertEqual(lll['msg'],self.shuju[0][1])

    def test_2(self):

        lll = self.tes_app(str(int(self.shuju[2][0])))
        self.assertEqual(lll['code'],str(int(self.shuju[2][2])))
        self.assertEqual(lll['msg'],self.shuju[2][1])
























