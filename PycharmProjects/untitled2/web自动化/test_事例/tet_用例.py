#! /usr/bin/env python
#! -*- coding:utf-8 -*-

import xlrd
import unittest
from web自动化.config.web_配置 import 配置_aa
from web自动化.data.读取_ex import duqu
from web自动化.data.读取_ex import duqu1





class 事例_tet(unittest.TestCase):
    aaa = 配置_aa().qq空间
    ff = duqu()




    def test_1(self):

        cc = self.aaa(int(self.ff[0][0]),self.ff[0][1])
        self.assertEqual(cc,'坏宝宝 [http://444205264.qzone.qq.com]')

    def test_2(self):

        cc = self.aaa(self.ff[1][0],self.ff[1][1])
        self.assertNotEqual(cc,'坏宝宝 [http://444205264.qzone.qq.com]')

    def test_3(self):

        cc = self.aaa(self.ff[2][0],self.ff[2][1])
        self.assertNotEqual(cc,'坏宝宝 [http://444205264.qzone.qq.com]')

    def test_4(self):

        cc = self.aaa(int(self.ff[3][0]),self.ff[3][1])
        self.assertNotEqual(cc,'坏宝宝 [http://444205264.qzone.qq.com]')

    def test_5(self):

        cc = self.aaa(int(self.ff[4][0]),self.ff[4][1])
        self.assertNotEqual(cc,'坏宝宝 [http://444205264.qzone.qq.com]')




class 京东_tet(unittest.TestCase):
    bb = 配置_aa().京东_j
    gg = duqu1()

    def test_1(self):

        ff = self.bb(self.gg[0])
        self.assertEqual(ff, '商品已成功加入购物车！')

    def test_2(self):

        ff = self.bb(self.gg[1])
        self.assertNotEqual(ff,'商品已成功加入购物车！')

    def test_3(self):

        ff = self.bb(self.gg[2])
        self.assertNotEqual(ff, '商品已成功加入购物车！')

    def test_4(self):
        ff = self.bb(self.gg[3])
        self.assertNotEqual(ff, '商品已成功加入购物车！')








if __name__ == '__main__':
    unittest.main()







