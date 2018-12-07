

# a = [1,5,3,5,9,9,9,9,7,8,8,666,900]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
#         b.sort()
#         b.reverse()
# print(b[0],b[1])
# for j in a:
#     if j == b[0]:
#         print(j)
#     if j == b[1]:
#         print(j)







# a = int(input('>>>'))
# b = int(input('>>>'))
# c = int(input('>>>'))
# f = [a,b,c]
# f.sort()
# if f[0] + f[1] > f[2]:
#     print('三角形')
#     if f[0]**2 + f[1]**2 < f[2]**2:
#         print('钝角')
#     elif f[0]**2 + f[1]**2 > f[2]**2:
#         print('锐角')
#     elif f[0]**2 + f[1]**2 == f[2]**2:
#         print('直角')
#     else:
#         print('no')



# a = [5,1,6,4,2,1,5,6]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
#         b.sort()
# print(b)



# a = input('>>>')
# b = len(a)                     # len() 统计某数据类型中有多少元素
# for i in range(b):
#     if a[i] != a[-i-1]:
#         print('不是回文')
#         break
# else:
#     print('回文')



# def aaa(x):
#     for i in range(len(x)-1):
#         for j in range(len(x)-i-1):
#             if x[j] > x[j+1]:
#                 x[j],x[j+1]=x[j+1],x[j]
#     print(x)
#
#
# aaa([5,1,6,3,2,7,8,9,2,1,2])



# def aaa(x):
#     for i in range(len(x)):
#         b=0
#         for j in range(len(x)-i):
#             if x[b] > x[j]:
#                 b = j
#                 x[b],x[j-1] = x[j-1],x[b]
#     print(x)
#
#
#
# aaa([5,7,4,2,1,3,5])


# a = int(input('输入资产：'))
# while True:
#
#     if a < 1000000000:
#         print({'name':'电脑','price':1999})
#         print({'name':'鼠标','price':10})
#         print({'name':'游艇','price':20})
#         print({'name':'美女','price':998})




# a = '123456'
# b = ','.join(a)
# c = b.split(',')
# c.reverse()
# s = 0
# for i,j in enumerate(c):
#    print(i,j)
#    for q in range(10):
#        if str(q)==j:
#            q = q*10**i
#            s = s+q
# print(s)
#









# b = '123456789'


# c = open(r'C:\Users\fxs\Desktop\b.txt','w',encoding='utf-8')
# for a in range(1,10):
#     for b in range(1,a+1):
#         c.write('{}*{}={}'.format(a,b,a*b)+'\t')
#     c.write('\n')
# c.close()


# for i in range(10):








# b = 'abcdefghijklmnopqrstuv'
#
#
# a = open('C:\\Users\\fxs\\Desktop\\z.txt','w',encoding='utf-8')
# a.write(b+'\n')
# a.write('sadasda'+'\n')
# a.write('zxcvbnm'+'\n')
# a.close()





# a = open('C:\\Users\\fxs\\Desktop\\aaa.jpg','rb')
# b = a.read()
# a.close()
#
#
# c = open('a.txt','wb')
# c.write(b)
# c.close()



# with open('b.txt','a',encoding='utf-8') as b:
#     b.write('123456')

# q='''11111111111111
# sadasd
# asdadasd
# asdadad
# asdasa
# '''
#
# with open('b.txt','a',encoding='utf-8') as a:
#     a.write(q+'\n')



# with open('b.txt','r',encoding='utf-8') as a:
#     b = a.readlines()
#     c = len(b)
#     print(c)
#     for i in b:
#         if '\n' == i:
#             b.remove(i)
#             c = len(b)
#     print(c)
#         if i.startswith('#'):
#             b.remove(i)
#             c = len(b)
#     print(c)






# with open('b.txt','r',encoding='utf-8') as a:
#     dd = a.readlines()
# for i in dd:
#     if i=='\n' or i.startswith('#'):
#         dd.remove(i)
#         c=len(dd)
# print(c)



# b='147'
# for i in range(1,11):
#     with open('{}q.txt'.format(i),'w',encoding='utf-8') as a:
#         for j in range(1,11):
#             a.write(str(j)+'\n')
















# a = '142536'
# b = '789123'
# a = a+b
# print(a)


# a = [1,5,2,4]
# b = '4125'
# a.append(b)
# print(a)

# a = [1,5,3,4,9]
# a.insert(1,'asd')
# print(a)










































