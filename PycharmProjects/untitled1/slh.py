




class poi():
    def zhishu(self,a,b):
        sun = 0
        for i in range(a,b):
            for j in range(2,i+1):
                if i % j == 0:
                    break
            if i == j:
                sun = sun+j
        print(sun)

    def huiwen(self,x):
        b = len(x)
        i = 0
        while i < b:
            if x[i] != x[-i-1]:
                print('失败')
                break
            i=i+1
        else:
            print('成功')


cc = poi()
cc.zhishu(100,200)
cc.huiwen('asddsa')




# class Asuna():
#     def jiec(self,a):
#         num = 1
#         sum = 0
#         i = 1
#         while i <= a:
#             num=num*i
#             sum=sum+num
#             i=i+1
#         print(sum)
#
#     def jiujiu(self,a,b):
#             for i in range(a,b):
#                 for j in range(1,i+1):
#                     print('{}*{}={}'.format(j,i,i*j),end='\t')
#                 print()
#
#
# aa = Asuna()
# aa.jiec(3)
# aa.jiujiu(1,10)





















