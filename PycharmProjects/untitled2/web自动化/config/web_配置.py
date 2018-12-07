#! /usr/bin/env python
#! -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
import unittest









class 配置_aa():

    def qq空间(self,zhang,mi):
        dr = webdriver.Chrome()
        dr.get('https://qzone.qq.com/')
        sleep(1)
        a = dr.find_element_by_xpath('//*[@id="login_frame"]')
        dr.switch_to.frame(a)
        dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(3)
        dr.find_element_by_xpath('//*[@id="u"]').send_keys('{}'.format(zhang))
        sleep(1)
        dr.find_element_by_xpath('//*[@id="p"]').send_keys('{}'.format(mi))
        sleep(1)
        dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(1)
        # c = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
        # dr.switch_to.frame(c)
        # kk = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]/div[4]')
        # sleep(2)
        # ActionChains(dr).drag_and_drop_by_offset(kk,185,0).perform()
        # sleep(2)
        return dr.title









    def 京东_j(self,kkk):
        dr = webdriver.Chrome()
        dr.get('https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_9fea7cddf389432997631dceec8773bb')
        sleep(1)
        dr.find_element_by_xpath('//*[@id="key"]').send_keys('{}'.format(kkk))
        sleep(1)
        dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        sleep(1)
        dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[7]/a[3]').click()
        sleep(2)
        pp = dr.current_window_handle
        wd = dr.window_handles
        for i in wd:
            if pp != i:
                dr.switch_to.window(i)
        aa = dr.find_element_by_xpath('//*[@id="result"]/div/div/div[1]/div[1]/h3').text
        return aa












aa = 配置_aa()
print(aa.京东_j())









