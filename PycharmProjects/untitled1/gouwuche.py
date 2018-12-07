
#/usr/bin/env python
# -*-coding:utf-8 -*-

# gg=int(input('请输入总资产'))
# print('wellcome')
# b=[{'name':'电脑','price':1999},{'name':'鼠标','price':10},{'name':'游艇','price':20},{'name':'美女','price':998}]
# d=len(b)
# e=[]
# for i,j in enumerate(b):
#     print(i,j['name'],j['price'])
#     continue
# while True:
#     a=int(input('请输入编号'))
#     print(b[int(a)])
#     e.append(b[int(a)])
#     print('已加入购物车')
#     t=input('是否购买此商品')
#
#     while True:
#         if t=='否':
#             break
#         if t=='是':
#             if int(b[a]['{}'.format('price')])<gg:
#                 gg-=int(b[a]['{}'.format('price')])
#                 print('你选购商品的价格为{}账户余额为{}'.format(b[a]['{}'.format('price')],gg))
#                 break
#             if b[a]["{}".format('price')] > gg:
#                 print('你的账户余额不足，无法购买')
#                 k=input('是否充值账户')
#                 if k=='否':
#                     break
#                 if k=='是':
#                     o=int(input('请输入充值金额'))
#                     gg+=o
#                     if int(b[a]['{}'.format('price')]) < gg:
#                         gg -= int(b[a]['{}'.format('price')])
#                         print('你选购商品的价格为{}账户余额为{}'.format(b[a]['{}'.format('price')], gg))
#                         break
#                         gg -= int(b[a]["{}".format('price')])
#                         print('成功充值{}，购买成功，账户当前余额为{}'.format(o,gg))
#     for p,q in enumerate(e):
#         print('购物车：{}'.format(q))
#     for u,i in enumerate(e):
#         print(u,i)
#         a=input('是否删除商品')
#         if a=='是':
#             e=list(e)
#             e.clear()
#             print('以删除购物车',e)
#         continue
#     if a=='否':
#         continue
#     else:
#         continue









#购物车

# jine = int(input('请输入总资产：'))
# goods = [{'name':'电脑','price':1999},
#          {'name':'鼠标','price':10},
#          {'name':'游艇','price':20},
#          {'name':'美女','price':998}]
#
# for i,j in enumerate(goods):
#     print(i+1,j['name'],j['price'])
# a = input('是否购买东西？买：是；不买：exit')
# while True:
#     if a == 'exit':
#         break
#     else:
#         gouwuche = []
#     # a=int(input('请输要购买的物品的编号：'))
#     # # print(goods[a])
#     # gouwuche.append(goods[a-1])
#     # print('已加入购物车')
#     # q = input('是否购买，请输入是或否：')
#         while True:
#             q = input('是否要买')
#             if q=='否':
#                 break
#             else:
#                 gouwuche.append(goods[int(q)-1])
#                 print('输入"否"退出')
#     while True:
                # if int(goods[a-1]['{}'.format('price')]) < jine:
                #     jine=jine-int(goods[a-1]['{}'.format('price')])
                #     print('你选购商品的价格为{}账户余额为{}'.format(goods[a-1]['{}'.format('price')],jine))
                #     break
                # if goods[a-1]["{}".format('price')] > jine:
                #     print('你的账户余额不足，无法购买')
                #     k = input('是否充值账户')
        #             if k=='否':
        #                 break
        #             if k=='是':
        #                 o = int(input('请输入充值金额'))
        #                 jine=jine+o
        #                 if int(goods[a-1]['{}'.format('price')]) < jine:
        #                     jine = jine - int(goods[a-1]['{}'.format('price')])
        #                     print('你选购商品的价格为{}账户余额为{}'.format(goods[a]['{}'.format('price')], jine))
        #                     break
        #                     gg -= int(b[a]["{}".format('price')])
        #                     print('成功充值{}，购买成功，账户当前余额为{}'.format(o,gg))
        # for n,m in enumerate(gouwuche):
        #     print('购物车：{}'.format(m))
        # for u,l in enumerate(gouwuche):
        #     print(u,l)
        #     aa = input('是否删除商品')
        #     if aa=='是':
        #         gouwuche=list(gouwuche)
        #         gouwuche.clear()
        #         print('以删除购物车',gouwuche)
        #     continue
        # if aa=='否':
        #     continue
        # else:
        #     continue



























goods = [{'name':'商品1','price':'1000'},
         {'name':'商品2','price':'2000'},
         {'name':'商品3','price':'3000'},
         {'name':'商品4','price':'4000'}]

b=int(input("总额"))
for i,j in enumerate(goods):
    print(i,j["name"],j["price"])
a=input("买东西吗，输入exit不买")
while True:
    if a=="exit":
        break
    else:
        car=[]
        while True:
            c = input("加入购物车，结束请输入exit")
            if c=='exit':
                break
            else:
                car.append(goods[int(c)])
                print('输入exit退出')
    while True:
            for d,f in enumerate(car):
                print(f["name"],f["price"])
            q=input("退货del，买完了输OK")
            if q=="del":
                    gg =int(input('请输入编号:'))
                    car.remove(car[gg])
                    print(car[int(c)])
            elif q=="ok":
                    break
    w=input("输入ok结账")
    sum=0
    if w == 'ok':
            for k,v in enumerate(car):
                    sum+=f['price']
                    print('消费金额',sum)
            if sum<=b:
                    print('购买成功')
                    b=b-sum
                    break
            else:
                    print('余额不足请充值')
                    r=int(input('输入金额:'))
                    b+=r
                    print('余额:',b)


















# goods = [{'name':'商品1','price':'1000'},
#          {'name':'商品2','price':'2000'},
#          {'name':'商品3','price':'3000'},
#          {'name':'商品4','price':'4000'}]
# aaa = int(input('总额：'))
# for i,j in enumerate(goods):
#     print(i+1,j['name'],j['price'])
# gouwuche=[]
#
# while True:
#     b = input('是否要购买，请输入是或否：')
#     if b=='否':
#         break
#     if b=='是':
#         c=int(input('根据序号加入购物车：'))
#         gouwuche.append(goods[c-1])
#         # print(gouwuche)
#     x=0
#     c=[]
#     for o in range(len(gouwuche)):
#         aa=gouwuche[o]['price']
#         c.append(aa)
#     for oo in c:
#        x=x+oo
#     print('所选商品总额',x)
# while True:
#     xx=input('请问你要购买吗？如果购买选择是，如果不购买则选择否：')
#     if xx == '否':
#         break
#     if xx == '是':
#         if x > aaa:
#             print('余额不够，是否充值？如果充值，则输入充值，若不充值则输入结束')
#         if x <= aaa:
#             qq = x-aaa
#             print('购买成功，余额显示',qq)


























