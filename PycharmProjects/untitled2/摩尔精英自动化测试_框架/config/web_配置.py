#! /usr/bin/env python
#! -*- coding:utf-8 -*-



from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
import  selenium.webdriver.support.ui as ui





class 配置():
    def 打开_摩尔精英(self):
        dr = webdriver.Chrome()
        dr.get('http://www.moore.ren/')
        sleep(1)
        dr.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[3]/a[8]').click()
        sleep(2)
        oo = dr.current_window_handle
        lo = dr.window_handles
        for j in lo:
            if oo != j:
                dr.switch_to.window(j)
        sleep(2)
        return dr.title


    def 打开1(self):
        dr = webdriver.Chrome()
        dr.get('http://www.moore.ren/')
        sleep(1)
        dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[4]/div/li[1]').click()
        sleep(2)
        aa = dr.current_window_handle
        ee = dr.window_handles
        for i in ee:
            if aa != i:
                dr.switch_to.window(i)
        sleep(2)
        return dr.title


aa = 配置()
print(aa.打开1())








