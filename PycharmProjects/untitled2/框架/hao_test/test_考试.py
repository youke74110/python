#! /usr/bin/env python
#! -*- coding:utf-8 -*-





import unittest
# import xlrd
from 框架.config.学校_接口 import 学校_查询
from 框架.data.duqu_数据 import duqu1

class kaoshi1(unittest.TestCase):
    tes_学校=学校_查询().学校_快查
    shuju=duqu1()

    def test_1(self):

        lll = self.tes_学校(self.shuju[0][0])
        self.assertEqual(lll['code'],int(self.shuju[0][1]))
        self.assertNotEqual(len(lll['data']),int(self.shuju[0][2]))
        # self.assertEqual(lll['data'][0]['schoolName'],list)

    def test_2(self):

        lll = self.tes_学校(self.shuju[1][0])
        self.assertEqual(lll['code'],int(self.shuju[1][1]))
        self.assertEqual(len(lll['data']),int(self.shuju[1][2]))


    def test_3(self):

        lll = self.tes_学校(self.shuju[2][0])
        self.assertEqual(lll['code'],int(self.shuju[2][1]))







