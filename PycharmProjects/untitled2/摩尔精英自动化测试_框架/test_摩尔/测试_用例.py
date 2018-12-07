#! /usr/bin/env python
#! -*- coding:utf-8 -*-


import unittest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
import  selenium.webdriver.support.ui as ui

from 摩尔精英自动化测试_框架.config.web_配置 import 配置






class 测试_用例_1(unittest.TestCase):

    def test_1(self):
        aaa =配置().打开_摩尔精英

        self.assertEqual(self.aaa(),'摩尔芯闻-全球半导体内参-半导体新闻-摩尔半导体指数新鲜发布')



    def test_2(self):
        bb = 配置().打开1

        self.assertEqual(self.bb(),'上海半导体职位-半导体招聘-半导体人才网-摩尔精英招聘')

    # def test_3(self):



