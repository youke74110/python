#! /usr/bin/env python
#! -*- coding:utf-8 -*-

import requests
import re

class app_接口():
    def app_接口1(self,a):
        url = 'http://www.zhaoapi.cn/user/getDefaultAddr'
        querystring = {'uid':'{}'.format(a)}

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'}

        res = requests.get(url=url, headers=headers, params=querystring)
        # print(res.json())
        html = res.json()
        return html


print(app_接口())


