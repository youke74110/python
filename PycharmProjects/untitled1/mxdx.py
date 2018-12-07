


# class Lei():
#     def aaa(self):
#         a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
#         b = 100
#         f = ''
#         while True:
#             c = b % 16
#             b = b // 16
#             f = f + a[c]
#             if b == 0:
#                 break
#         print(f[::-1])
#
#     def jiu(self):
#         for i in range(1, 10):
#             for j in range(1,i+1):
#                 print('{}*{}={}'.format(i,j,i*j),end='\t')
#             print()




# w = Lei()
#
# w.aaa()
# w.jiu()





# str

# object


# class Dmc():
#     def poio(self):
#         # b = self.ee()
#         sum=0
#         for i in range(1,6):
#             sum = sum+i
#         return sum
#     def yamato(self):
#         # b = self.poio()
#         s = 1
#         for p in range(1,5):
#             s = s*p
#         return s
#
#
#
# a = Dmc()
# print(a.yamato())






# class Xin():
#      def poi(self):
#          return 789

# x = xin()
# print(x.ww())
# print(x.ee())






# class Gxin(Xin,Dmc):
#     def poi(self):
#         pp = 0
#         for k in range(1,101):
#             pp = pp+k
#         return pp
#
# o = Gxin()
#
# print(o.poio())




# class Asuna():
#     def __init__(self,a,b):         #初始化属性
#         self.a = a
#         self.b = b
#     def poi(self,a):
#         print('hello %s，今年%d年级'%(self.a,self.b))
#     def kirito(self):
#         print('hello %s,只有15岁'%(self.a))
#
#
#
# aa = Asuna('Kirito',9)
# aa.poi(415263)
# aa.kirito()
# aa = Asuna('大和',10)
# aa.poi()
# aa.kirito()
# aa = Asuna('响',5)
# aa.poi()
# aa.kirito()





class biao():
    def __init__(self,name,xuel,zhanl):
        self.name = name
        self.xuel = xuel
        self.zhanl = zhanl
    def daguai(self):
        self.xuel -= 500
    def xiulian(self):
        self.xuel += 1000
    def juedou(self):
        self.xuel -= 1000
    def print_xue(self):
        print('%还有%血，还有%d战力'%(self.name,self.xuel,self.zhanl))


aa = biao('kirito',2000,500000)
aa.daguai()
aa.




























