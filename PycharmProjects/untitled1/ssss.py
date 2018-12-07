#导入正则模块
#只能匹配字符串（只能过滤字符串）
#贪婪模式，非贪婪模式
#贪婪模式：尽可能多的去匹配最后的字符串
#非贪婪模式：尽可能少的去匹配最后的字符串
#带?的是非贪婪，带*的是贪婪
#.匹配任意一个字符，除了换行符




import re
a = 'asd147asdasd789asd'
#将要匹配的正则编译
b = re.compile('asd(.*)asd',re.S)
#到目的字符串中去查找
c = b.findall(a)
print(c)



l = '''asd123147
asdasdQWE123123asdasdQWE741258asd'''
k = re.compile('asd(.*?)asd',re.S)
#re.S 让.可以匹配包括换行符在内的所有字符
#re.I 匹配的字符不区分大小写
j = k.findall(l)
print(j)











