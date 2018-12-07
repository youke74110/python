

import pymysql





#a=8
#if a<5:
#    print('你好')
#else:
#    print('不好')





#a=5
#b=8
#if b == a+3:
#    print('你好')
#else:
#    print('hello')



# a = input('请输入成绩')
# b = int(a)
# if b > 90 and b <= 100:
#     print('优秀')
# elif b > 80 and b <= 90:
#     print('良好')
# elif b >= 70 and b <= 80:
#     print('及格')
# elif b < 70:
#     print('菜')



# a = input('手动输入字符串')
# if a.startswith('a'):
#     if a.endswith('c'):
#         print('hello word')
#     else:
#         print('hello')
# elif a.endswith('c'):
#     print('word')
# else:
#     print('123')



# a = input(' ')
# if a.startswith('a'):
#     print("asd")


# a= input('手动输入字符串')
# if a.startswith('a'):
#     if a.endswith('c'):
#         print('hello word')
#     else:
#         print('hello')
# elif a.endswith('c'):
#     print('word')
# else:
#     print('123')



# a = input('手动输入字符串：')
# if a.startswith('a') and a.endswith('c'):
#     print('hello word')
# elif a.startswith('a'):
#     print('hello')
# elif a.endswith('c'):
#     print('word')
# else:
#     print('123')





# a = input('输：')
# s = input('输：')
# d = input('输：')
# z = int(a)
# x = int(s)
# c = int(d)
# f = [z,x,c]
# f.sort()
# if  f[0] + f[1] > f[2]:
#     if f[0] + f[2] > f[1]:
#         if f[1] + f[2] > f[0]:
#             print('三角形')
# else:
#     print('不是三角形')




# a = [3,4,5]
# a.sort()
# if a[0]+a[1]>a[2]:
#     if a[0]**2+a[1]**2 <a[2]**2:
#         print('钝角')
#     elif a[0]**2+a[1]**2 >a[2]**2:
#         print('锐角')
#     elif a[0]**2+a[1]**2 ==a[2]**2:
#         print('直角')
# else:
#     print('123')




# a = 20
# for i in range(0,a,2):
#     print(i)


# a = 101
# s = 0
# for i in range(a):
#     s=s+i
# print(s)


# a = 0
# for i in range(1,101)
#     a+=i
#     print(a)



# a = {'qwe':123,'asd':147,'zxc':159}
# for i,j in a.items():
#     print(i,j)



# a = [123,147,159]
# for i in a:
#     print(i)



# a = 100
# s = 0
# d = 0
# for i in range(1,a,2):
#     s=s+i
# for f in range(0,a,2):
#     d=d+f
# c=s-d
# print(c)




#a = [142,5412,'qwes','asdc',142]
# a = '12452asda'
# for i in enumerate(a):
#     print(i)



# a = ['电脑','计算机','mp3']
# for i,j in enumerate(a):
#     print(i,j)
# b= input('输入')
# b= int(b)
# print(a[b])






# a = ['asd','qwe','zxc']
# for i in enumerate(a):
#     print(i)








# b = 0
# for i in range(1,100):
#     if i % 2 ==0:
#         b=b-i
#     else:
#         b=b+i
# print(b)



# a = random.randrange(1,10)    # 随机选取一个数字
# b = int(input('输入一个数字：'))



# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(j,i,i*j),end='')
#     print()




# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end='\t')
#     print()




# for i in range(1,10):
#     if i==6:
#         break
#     else:
#         print(i)



# for i in range(1,10):
#     if i==6:
#         continue
#     else:
#         print(i)




# a = ['123','qwe','as1','sda','asdd']
# for i in a:
#     if len(i)==2:
#         break
# else:
#     print('lll')



# a = random.randrange(1,10)
# for i in range(3):
#     b = int(input('输入：'))
#     if b == a:
#         break
#     elif b < a:
#         print('小了')
#     elif b > a:
#         print('大了')




# rando


# while True:
#     a = int(input('srsz'))
#     print(a)
#     b =[{'name':'电脑','price':1999},{'name':'鼠标','price':10},{'name':'游艇','price':20},{'name':'美女','price':998}]
#     for i,j in enumerate(b):
#         print(i,j)
        # if a > 'price':
        #     print('可购买')
        # if a < 'price':
        #     print('不可以')





asd = pymysql.connect(host='192.168.0.185',
                        port=3306,
                        user='root',
                        password='654321',
                        charset='utf8')

aaa = asd.cursor()




# aaa.execute('show databases;')
# aaa.execute('use fxs;')
# aaa.execute('show tables;')
# aaa.execute('select * from tx;')
# aaa.execute('show databases;')
# aaa.execute('use mmm;')
# aaa.execute('show tables;')
# aaa.execute('select * from uiu;')
# aaa.execute('create database xiao;')
# aaa.execute('show databases;')
# aaa.execute('drop database test1;')
# aaa.execute('show databases;')
# aaa.execute('use xiao;')
# aaa.execute('create table xxtx(name char(30),sex char(20),age int);')
# aaa.execute('desc xxtx')
# aaa.execute('insert into xxtx values("","女",21)')
# aaa.execute('select * from xxtx')

# print(aaa.fetchall())



# aaa.close()

# aaa.execute('show database;')
# aaa.execute('use xiao;')
# aaa.execute('show tables;')
# aaa.execute('select * from uiu;')
# print(aaa.fetchall())
#















































# aaa.execute('show databases;')       # 执行sql语句
# aaa.execute('use fxs;')
# aaa.execute('show tables;')
# aaa.execute('select * from tx;')
#
#
# # print(aaa.fetchall())                # 读取上一句sql语句的结果
#
# # print(aaa.fetchmany(3))               # 读取上一句sql语句的结果，括号里写多少，就
#                                        # 读取多少，不写默认一个
#
#
# print(aaa.fetchone())                  #每次读取一个结果，本身有迭代功能
# print(aaa.fetchone())
# print(aaa.fetchone())
# print(aaa.fetchone())



# aaa.execute('create database mmm;')
# aaa.execute('use mmm;')
# aaa.execute('create table uiu(姓名 char(30),年龄 int, 班级 char(20));')
# list1 = ['小李',1,'测试班']
# for i in range(30):
#     aaa.execute('insert into uiu values("{}",{},"{}");'.format(list1[0],list1[1],list1[2]))
#     asd.commit()
#
# aaa.execute('select * from uiu;')
# for i in aaa.fetchall():
#     print(i)




# aaa.execute('use mmm;')
# aaa.execute('show tables;')
# aaa.execute('select * from uiu;')
# # print(aaa.fetchall())
# b= aaa.fetchall()
# # print(b)
# with open('b.txt','w',encoding='utf-8') as f:
#     for i in b:
#         f.write('\n'+'{},{},{}'.format(i[0],i[1],i[2]))

























