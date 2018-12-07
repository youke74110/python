 shopping_car =[]
 product_list_tatol = "---product list----"
 welcome = "-----------welcome to shopping marketi----------"
 product_list = [
     ('iphone',5888),
     ('lenovo',998),
     ('cup',12),
     ('thinkpad',4500),
    ('notebook',6)
 ]
 print welcome
 salary = raw_input("input your salary:>>>")
 if salary.isdigit():
     salary = int(salary)
 while True:
    print product_list_tatol
     for item in product_list:
         print product_list.index(item)+1,item
     choice = raw_input("choice you want to buy:>>> ___   0 to exit")
     if choice.isdigit():
         choice = int(choice)
     if choice > 5 or choice < 0:
         print  "no this goods,请重新选择"
         continue
     elif choice <=5 and choice >=1:
        if salary < product_list[choice-1][1]:
             print "账户余额不足，请购买其他商品或者退出"
             continue
         else:
             pass
         item_choice = product_list[choice-1]
         shopping_car.append(item_choice)
         print "you buy goods is", shopping_car
         salary = salary - product_list[choice-1][1]
         print "your balance is %d"%(salary)

     elif choice == 0:
         print  "you buy goods is",shopping_car,
         print "your balance is %d"%(salary)
         exit()





















 product_list = [
     ('Mac', 9000),
     ('kindle', 800),
     ('tesla', 900000),
     ('python book', 105),
     ('bike', 2000),

 ]
 saving = input('please input your money:')
 shopping_car = []
 if saving.isdigit():
     saving = int(saving)
     while True:
         # 打印商品内容
         for i, v in enumerate(product_list, 1):
             print(i, '>>>>', v)

             # 引导用户选择商品
         choice = input('选择购买商品编号[退出：q]：')
         # 验证输入是否合法
         if choice.isdigit():
             choice = int(choice)
             if choice > 0 and choice <= len(product_list):
                 # 将用户选择商品通过choice取出来
                 p_item = product_list[choice - 1]
                 # 如果钱够，用本金saving减去该商品价格，并将该商品加入购物车
                 if p_item[1] < saving:
                     saving -= p_item[1]
                     shopping_car.append(p_item)
                 else:
                     print('余额不足，还剩%s' % saving)
                 print('你已经购买商品''>>>>>>', p_item)
             else:
                 print('编码不存在')
         elif choice == 'q':
             print('------------您已经购买如下商品----------------')
             # 循环遍历购物车里的商品，购物车存放的是已买商品
             for i in shopping_car:
                 print(i)
             print('您还剩%s元钱' % saving)
             break
         else:
             print('invalid input')











