#! /usr/bin/env python
#! -*- coding:utf-8 -*-

import requests



class 学校_查询():
    def 学校_快查(self,a):
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        querystring = {'filterInput': '{}'.format(a)}

        headers = {
            'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA',
            'Content-Type': 'application/x-www-form-urlencoded'}

        res = requests.get(url=url, headers=headers, params=querystring)
        # print(res.json())
        html = res.json()
        return html

    def 学校_考试_快查(self,b):
        pass
    def 学校_列表(self):
        pass





