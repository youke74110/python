
#  接口测试





import xlrd
import requests
import unittest
import HTMLTestRunne
import HTMLTestRunnertest
import time










# class xuexiao():
def aaa(a):
    url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
    querystring = {'filterInput':'{}'.format(a)}

    headers = {'cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA',
                'Content-Type':'application/x-www-form-urlencoded'}

    res = requests.get(url = url,headers = headers,params = querystring)
    # print(res.json())
    html = res.json()
    return html





# a = xuexiao()
#
# print(a.aaa('北京'))


##断言
# assert html['code'] ==0





# class xuexiao1(unittest.TestCase):
#     def setUp(self):      ## 主要的作用：初始化测试环境。    每次执行测试用例前执行
#         print(123)
#
#     def tearDown(self):    ## 清理环境   每次用例执行之后去执行
#         print(1477)
#
#     def test_1(self):
#         print('a')
#
#     def test_2(self):
#         print('b')
#
# unittest.main()







# f = xlrd.open_workbook(r'C:\Users\fxs\Desktop\asddsa.xlsx')
# sheet = f.nsheets
# sheet = f.sheets()[0]
# pp = sheet.col_values(0)
# print(pp[0])
#
# for i in pp:
#     print(i)





# class xuexiao1(unittest.TestCase):
#     def setUp(self):      ## 主要的作用：初始化测试环境。    每次执行测试用例前执行
#         print('开始')
#
#     def tearDown(self):    ## 清理环境   每次用例执行之后去执行
#         print('结束')
#
#
#     def test_1(self):
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#         f = xlrd.open_workbook(r'C:\Users\fxs\Desktop\asddsa.xlsx')
#         sheet = f.nsheets
#         sheet = f.sheets()[0]
#         pp = sheet.col_values(0)
#         # print(pp[0])
#
#         for i in pp:
#             # print(i)
#
#
#             querystring = {'filterInput': '{}'.format(i)}
#
#             headers = {
#                 'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA',
#                 'Content-Type': 'application/x-www-form-urlencoded'}
#
#             res = requests.get(url=url, headers=headers, params=querystring)
#             # print(res.json())
#             html = res.json()
#             print(html['code'])
#
#     def test_2(self):
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#         f = xlrd.open_workbook(r'C:\Users\fxs\Desktop\asddsa.xlsx')
#         sheet = f.nsheets
#         sheet = f.sheets()[0]
#         pp = sheet.col_values(0)
#         # print(pp[0])
#
#         for j in pp:
#         # print(i)
#
#             querystring = {'filterInput': '{}'.format(j)}
#
#             headers = {
#                 'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA',
#                 'Content-Type': 'application/x-www-form-urlencoded'}
#
#             res = requests.get(url=url, headers=headers, params=querystring)
#             # print(res.json())
#             html = res.json()
#             print(html['data'])
    # def test_3(self):
    #     url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
    #     f = xlrd.open_workbook(r'C:\Users\fxs\Desktop\asddsa.xlsx')
    #     sheet = f.nsheets
    #     sheet = f.sheets()[0]
    #     pp = sheet.col_values(0)
    #     # print(pp[0])
    #
    #     for j in pp:
    #         # print(i)
    #
    #         querystring = {'filterInput': '{}'.format(j)}
    #
    #         headers = {
    #             'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA',
    #             'Content-Type': 'application/x-www-form-urlencoded'}
    #
    #         res = requests.get(url=url, headers=headers, params=querystring)
    #         # print(res.json())
    #         html = res.json()
    #         print(html['code'])
#
#
# unittest.main()













class xuexiao1(unittest.TestCase):
    # def setUp(self):      ## 主要的作用：初始化测试环境。    每次执行测试用例前执行
    #     print('开始')
    #
    # def tearDown(self):    ## 清理环境   每次用例执行之后去执行
    #     print('结束')

    def shuju(self):
        shuju1 = []
        f = xlrd.open_workbook('asdasd.xlsx')
        # sheet = f.nsheets
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(1,num):
            oo = sheet.row_values(i)
            shuju1.append(oo)
        # pp = sheet.col_values(0)
        return shuju1

    def test_1(self):
        shu = self.shuju()
        lll = aaa(shu[0][0])
        self.assertEqual(lll['code'],int(shu[0][1]))
        self.assertEqual(len(lll['data']),int(shu[0][2]))
        # self.assertEqual(lll['data'][0]['schoolName'],list)

    def test_2(self):
        shu = self.shuju()
        lll = aaa(shu[1][0])
        self.assertEqual(lll['code'],int(shu[1][1]))
        self.assertEqual(len(lll['data']),int(shu[1][2]))


    def test_3(self):
        shu = self.shuju()
        lll = aaa(shu[2][0])
        self.assertEqual(lll['code'],int(shu[2][1]))


    # def test_4(self):
    #     lll = aaa('$#@')
    #     self.assertNotEqual(lll['code'],1)

if __name__=='__main__':
    # unittest.main()
    # 生成测试报告 创建一个测试套件
    suit = unittest.TestSuite()
    # 1.添加测试用例,将测试用例添加到测试套件中

    # suit.addTest(xuexiao1('test_1'))
    # suit.addTest(xuexiao1('test_2'))
    # suit.addTest(xuexiao1('test_3'))
    # suit.addTest(xuexiao1('test_4'))

    # 2.将整个类中的所有测试用例添加到测试套件中
    suit.addTest(unittest.makeSuite(xuexiao1))
    now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    with open('all3.html','wb') as f:
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='fxs',
                                                   description = '测试结果如下：',
                                                   title = '好分数测试报告',
                                                   stream = f)
        runner.run(suit)
        f.close()















































# import requests

# while True:
# a =input('>>>')
# url='http://testsupport-be.haofenshu.com/v1/schools/infos?filterInput={}'.format(a)
#
# head={
#     'cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
# }
# re=requests.get(url=url,headers=head)
# html=re.content.decode('utf-8')
# print(re.json())







