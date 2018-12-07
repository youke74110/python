








# 1.
#
# def aaa():
#     sun=0
#     for i in range(2,100):
#         for j in range(2,i+1):
#             if i % j ==0:                   ##100以内的质数之和
#                 break
#         if j == i:
#             sun = sun + i
#     print(sun)







# print(__name__)



# if __name__ == '__main__':
#     print('asdasd')
#     print('123456')



# 2.
# def aaa(x):
#     a = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
#     b = x
#     f = ''
#     while True:
#         c=b%16
#         b=b//16
#         f=f+a[c]               ###  十进制转十六进制
#         if b == 0:
#             break
#     print(f[::-1])



# 3.
# def jiu(x=6):
#     for i in range(1,x+1):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(i,j,i*j),end='\t')
#         print()                                         ##  函数，九九乘法表






# 4.
# def jia():
#     sum=0
#     i=0
#     while i<=100:
#         sum=sum+i            ##  函数  100以内所有数相加
#         i=i+1
#     print(sum)







# 5.
# def aaa(a='asd'):
#     b = len(a)
#     i = 0
#     while i < b:
#         if a[i] != a[-i-1]:
#             print('失败')
#             break                  ##  函数，字符串回文
#         i=i+1
#     else:
#         print('成功')



# 6.
# def aaa(a):
#     for i in a:
#         for j in a:
#             for x in a:
#                 if i!=j and i!=x and j!=x:    ## 四个数 组成不同的三位数
#                     # print(i,j,x)
#                     print(i*10**2+j*10**1+x*10**0)
#
#
#
# aaa([1,2,3,4])



# 7.
# def uuu(a):
#     sum=0
#     for i in range(a+1):
#         sum=sum+i                     ##任意数以内的和
#     print(sum)
#
#
# uuu(100)





# 8.
def ppp():
    













