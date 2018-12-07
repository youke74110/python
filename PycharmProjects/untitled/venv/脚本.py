# /usr/bin/env python
# -*- coding:utf -8 -*-
import random



# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end='\t')
#     print()




# 质数之和
# def aaa():
#     sun=0
#     for i in range(100,200):
#         for j in range(2,i+1):
#             if i % j ==0:
#                 break
#         if j == i:
#             sun = sun + i
#     print(sun)
#     # print(j)
#
#
# aaa()





# 阶乘之和
# a = input('输入：')
# a = int(a)
# num = 1
# sum = 0
# i = 1
# while i <= a:
#     num=num*i
#     sum=sum+num
#     i=i+1
# print(sum)


# 阶乘之和
# sum = 0
# num = 1
# for i in range(1,5):
#    num = num * i
#    sum = sum + num
# print(sum)






# 去重排序
# a = [1,4,2,1,3,4,5,1,9]
# a =set(a)
# a =list(a)
# a.sort()
# print(a)


# a=1
# while a<=3:
#    a=a+1
#    print('aaa')


# a = 1
# sum=0
# while a <= 100:
#     sum=sum+a
#     a=a+1
# print(sum)



# a = random.randrange(1,10)
# i = 0
# while True:
#     b = int(input('输入数字：'))
#     if b == a:
#         print('成功')
#         break
#     elif b < a:
#         print('小')
#     elif b > a:
#         print('大')
#         i=i+1

# b = 1
# while b<=9:
#     a = 1
#     while a<=b:
#         print('{}*{}={}'.format(a,b,a*b),end='\t')
#         a=a+1
#     b=b+1
#     print()


# a = 1
# while a<=9:
#     b = 1
#     while b<=a:
#         print('{}*{}={}'.format(a,b,a*b),end='\t')
#         b= b+1                                      ## 九九乘法表
#     a=a+1
#     print()


# a = 0
# i = 2
# while i <= 100:
#     b = 2
#     while b <=i:
#         if i % b ==0:     ###质数之和
#             b=b+1
#             i=i+1
#             break
#     if i==b:
#         a=a+b
#     print(a)



# a = [1,25,78,12]
# print(sum(a))

# a = ['1','147','142']
# b = int(a[1])
# print(type(b))


# while True:
#     a = input('asd')
#     if a == 'exit':
#         break
#     b = a.split(',')
#     c = len(b)                     ### 一组数的平均数，比平均数小的数，输入exit结束
#     for i,j in enumerate(b):
#         b[i]=int(j)
#     print(sum(b)/c)
#     for v in b:
#         if v <sum(b)/c:
#             print(v)







# a = input('aaa')
# c = len(a)
# for i in range(c):
#     if a[i] != a[-i-1]:
#         print('xxx')                 ###字符串回文
#         break
# else:
#     print('zxc')





# a = input('asd')
# b = a.split(',')
# c = len(b)
# for i in range(1,c):
#         d=b[i]
#         b[i]=b[i-1]                 ###将列表中的元素向左挪一位
#         b[i-1]=d
# print(b)



















# for i in range(100,1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     d = a**3
#     f = b**3                     ###  水仙花数
#     h = c**3
#     j = d+f+h
#     if i == j:
#         print(i)




# a = '14253547415264214'
# b = a[::-1]
# s = 0
# for i,j in enumerate(b):
#     print(i,j)
#     for q in range(10):          ## 不用int将字符串变整数
#         if str(q) == j:
#             q=q*10**i
#             s=s+q
# print(s)





# a = [1,2,3,4,5,6]
# print(type(a[1]))








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

#
#
# aaa(200)







# a = input('aaa')
# b = len(a)
# i = 0
# while i < b:
#     if a[i] != a[-i-1]:       ###  字符串回文
#         print('失败')
#         break
#     i=i+1
# else:
#     print('成功')





# def jiu(x=6):
#     for i in range(1,x+1):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(i,j,i*j),end='\t')
#         print()                                         ##  函数，九九乘法表
#
#
# jiu(9)
#
#
#
# def jia():
#     sum=0
#     i=0
#     while i<=100:
#         sum=sum+i            ##  函数  100以内所有数相加
#         i=i+1
#     print(sum)


#
# jia()






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
#
#
#
# aaa()






# def asd(*args):
#     print(args)
#
#
# asd('asd',',','sdaad',[1,5,4,6,7],(14,52,4,1,5,'zxc'))


# def aad(**kwargs):
#     print(kwargs)
#
#
#
# aad(www=471,wwe=789)
# aad(qqr=785,poi=369)
# aad()



# def addf(x,y=5,*z):
#     print(x,y,z)
#
#
#
# addf(4,6,45,2,14,52,)




# a = [1,2,1,3,7,8,4,2,4,5,1,2]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
#         b.sort()
# print(b)



# a = [1,5,8,4,6,2,3,8,9,9]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)         ###取第一大和第二大值
#         b.sort()
#         b.reverse()
# print(b[0],b[1])




# def maopao(x):
#     for i in range(len(x)-1):
#         for j in range(len(x)-i-1):
#             if x[j] > x[j+1]:
#                 x[j],x[j+1]=x[j+1],x[j]     ## 冒泡排序，用函数
#     print(x)
#
# 
# maopao([1,5,6,7,2,4,9,7,3,5,5,8,9,3,7,6,8])



# def paixu(a):
#     for i in range(len(a)):
#         for j in range(len(a)-i):
#             if a[i] > a[j]:
#                 a[i],a[j]=a[j],a[i]       ##  选择排序，有问题，需要更改
#     print(a)
#
#
# paixu([1,5,9,4,6,3,2,7])











# s = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
#
# # select_sort
# for i in range(0, len(s) - 1):
#     index = i
#     for j in range(i + 1, len(s)):
#         if s[index] > s[j]:
#             index = j
#     s[i], s[index] = s[index], s[i]     ## 选择排序，有点问题
#
# # print sort result.
# for m in range(0, len(s)):
#     print(s[m])








# a = [1,5,2,41,2,1,3,5,2]
# b = []
# c =len(b)
# for i in a:
#     if i not in b:                ###  去重排序
#         b.append(i)
#         b.sort()
# print(b)




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

# a = [1,2,3,5]
# print(a)






# def quchong(x):
#     b=[]
#     for i in x:
#         if i not in b:
#             b.append(i)
#     print(b)
#
# quchong([1,2,5,9,4,3,2])





# a = 123
# def ccc():
#     global a
#     a = 147
#     print(a)
#
# print(a)
# ccc()
# print(a)




# def aaa():
#     b=0
#     for i in range(1,101):
#         b=b+i
#     print(b)
#     return b
#
# print(aaa()+5)




# a = lambda : 3 < 6
# print(a())

# a = lambda x,y : x+y
# b = lambda x,y : x-y
# c = lambda x,y : x*y
# d = lambda x,y : x//y
# aa = input('qqq')
# if '+' in aa:
#     print(a(int(aa[0],int(aa[1])))
#     elif '-' in aa:
#         print(b(int(aa[0],int(aa[1])))
#     elif '*' in aa:
#         print(c(int(aa[0],int(aa[1])))
#     elif '//' in aa:
#         print(d(int(aa[0],int(aa[1])))
# print(aa)



# def aaa(x,y):


# i=[1,5,6,4,2]
# i.sort()
# a = [q*9//2 for q in i if q>=1 and q<=2006]
# print(a)

# a = [1,2,4,8,5,3,1]
# print(max(a))
# print(min(a))



# a = 542
# print(hex(a))
# print(oct(a))
# print(bin(a))
# print(int(0o11101101111101111110001))



# a,b = divmod(45,5)
# print(a,b)






# for i in range(1,100):
#     a = 0
#     for j in range(1,i):
#         if i % j == 0:         ###因数之和
#             a=a+j
#     if a == i:
#         print(i)







# sun = 0
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i % j == 0:
#             break
#     if j == i:
#         sun=sun+i
# print(sun)




# a = [1,3,4,5]
# b = int(input('qqq'))
# a.append(b)
# a.sort()
# print(a)



# a=[1,3,4,5]
# b=int(input('qqq'))
# c=[]
# for i,j in enumerate(a):
#     if a[i] < b:
#         a.append(b)
# for k in a:
#     if k not in c:
#         c.append(a)
#         c.sort()
# print(c)




# a = [5,4,2,9,1,3]
# b = max(a)
# c = min(a)
# d =a.index(b)
# e =a.index(c)
# if a[d]!=a[0]:
#     if a[e]!=a[-1]:         ##把最大的放在最后，最小的放在第一位
#         b=a[0]              ##脚本有问题
#         c=a[-1]
#         print(a)
# for i,j in enumerate(a):
#     print(j)



# a = [1,5,6,7,1,2,9,9,4]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)












# a = [1,5,3,5,9,9,7,8,8]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
#         b.sort()
#         b.reverse()               ###打印一个列表中第一大和第二大的值
# print(b[0],b[1])
# for j in a:
#     if j == b[0]:
#         print(j)
#     if j == b[1]:
#         print(j)






# def aaa(x):
#     a=[1,4,9]
#     a.append(x)
#     a.sort()
#     print(a)
#     return
#
#
# aaa(2)






# a = [1,2,3,8,1,9]
# b=max(a)
# c=min(a)
# if c < a[0]:
#     c,a[0]=a[0],c
# if b > a[-1]:
#     b,a[-1]=a[-1],b
# print(a)


# a = [1,5,3,4,1,5,2]
# b = []
# for i in a:
#     if i not in b:
#         b.append(a)
#         b.sort()
# for j in a:
#     if b[0]==i:
#         i,a[0]=a[0],i
#     if b[-1]==i:
#         i,a[-1]=a[-1],i
# print(a)










# def aaa(x):
#     a=[1,2,4,5]
#     a.append(x)
#     a.sort()
#     print(a)
#
# aaa(4)




# def aaa(x):
#     a = [1,2,4,5]
#     b = x
#     for i,j in enumerate(a):
#         if a[i] < b:
#             if a[i+1] > b:
#                 a.append(b)
#                 a[i] = b
#
#     print(a)
#
#
# aaa(3)

# try:
#     a= [4,15,27]
#     b= [6,5,8]
#     a= a+b
#     print(a)
# except:
#     print('aaaa')



# try:
#     a='147'
#     print(a+1)
# except Exception or NameError as q:
#     print(q)



# try:
#     b='145555'
#     c=b+a
# except Exception as q:
#     print(q)
# else:
#     print(c)


# try:
#     a='147'
#     c=a+b
# except Exception as q:
#     print(q)
# else:
#     print(c)
# finally:
#     print('aaa')



# a = 147
# if a < 12:
#     raise TypeError('你犯错了')
# print(147+789)


# raise NameError('错错错')







# import day2


# from day2 import *











# def huiwen(a):
#     c = len(a)
#     for i in range(c):
#         if a[i] != a[-i-1]:
#             print('不')
#             break
#     else:
#         print('回')
#
# huiwen('asddsd')





























