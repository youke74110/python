
import pymysql





abc = pymysql.connect(host='192.168.0.156',
                      port=3306,
                      user='root',
                      password='654321',
                      charset='utf8')

aaa = abc.cursor()
while True:
    l = input('输入命令继续，输入exit结束：')
    if l='exit':
        break

# aaa.execute('show databases;')
aaa.execute('use xiao;')
# aaa.execute('show tables;')
# aaa.execute('select * from xxtx;')

# aaa.execute('create table tx(name char(30),sex char(30),age int);')
# aaa.execute('insert into tx values("","女",15);')
# aaa.execute('delete from tx where name="";')
aaa.execute('select * from tx;')

er = aaa.fetchall()

print(er)


















