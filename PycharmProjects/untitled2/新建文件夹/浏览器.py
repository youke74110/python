



import re
from selenium import webdriver
from time import sleep

# 动作链
from selenium.webdriver.common.action_chains import ActionChains
import  selenium.webdriver.support.ui as ui









dr = webdriver.Chrome()          # 打开浏览器
# dr.get('https://www.jd.com/')    # 请求网址
# sleep(3)


dr.get('http://www.moore.ren/')

# dr.maximize_window()
sleep(2)


dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[4]/div/li[1]/a').click()
sleep(2)



## 截图
# dr.get_screenshot_as_png()
# dr.save_screenshot('abc.png')          # 保存截图  括号里面写的是文件名

#  截图并保存
# dr.get_screenshot_as_file('aaa.png')


# dr.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[3]/a[8]').click()
# sleep(2)









## 强制等待   sleep(2)
## 智能等待  设置控制器dr等待

# wait = ui.WebDriverWait(dr, 10)
# wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="chipDesign-list"]/ul/li[1]/div[1]/div[1]/a').is_displayed())
#
# dr.find_element_by_xpath('//*[@id="searchform"]/input[1]').send_keys('软件测试')
# wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="chipDesign-list"]/ul/li[1]/div[1]/div[1]/a').is_displayed())




 # .is_displayed()   判断元素是否显示            结果： True  Flase
 # .is_enabled()     判断元素是否为灰化状态

# dr.find_element_by_xpath('//*[@id="userForm0"]/div[8]/span/label').click()
#
# un = dr.find_element_by_xpath('//*[@id="userForm0"]/input[2]').is_enabled()
#
# print(un)












# dr.find_element_by_id('kw').send_keys('开封')
# sleep(1)
# dr.find_element_by_id('su').click()
# sleep(3)
# dr.find_element_by_xpath('//*[@id="1"]/h3/a').click()
# sleep(3)
# dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[5]/div[1]/a[6]').click()
#
# sleep(3)








# pp = dr.current_window_handle                       #  获取当前窗口的句柄
# wd = dr.window_handles
#
# for i in wd:
#     if i != pp:
#         dr.switch_to.window(i)                      ## 根据句柄 切换窗口
# # print(dr.title)
#
# pp = dr.find_element_by_xpath('//*[@id="leftcolumn"]').find_elements_by_tag_name('a')
# for j in pp:
#     b = j.text
#     # print(b)
#     if '变量类型' in j.text:
#         j.click()
#         sleep(1)
#         # sleep(1)












































# dr.get('http://www.qzone.qq.com/')
#
# sleep(2)
#
# dr.switch_to_frame('login_frame')
#
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
#
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('11122234')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('11223344')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(10)
#
# sss = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
# dr.switch_to_frame(sss)
#
# ppp = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
#
#
# ActionChains(dr).drag_and_drop_by_offset(ppp,200,0).perform()
#
# sleep(2)































## 移动滚动条  属于浏览器的，JavaScript语言

#1. 根据页面的高度来移动滚动条
## 控制滚动条的JavaScript代码
## 10000 表示的是当前页面的高度
## 数字越大，滚动条越往下
# for i in range(0,10000,500):
# js = 'var q=document.documentElement.scrollTop=10000'
# dr.execute_script(js)     #执行JavaScript语句
#
# sleep(2)

#2. 根据定位到的元素来移动滚动条

# target = dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[2]/div[4]/div/div[2]')
# js = 'arguments[0].scrollIntoView();'
# dr.execute_script(js,target)
# sleep(2)




























# dr.get('http://www.alltuu.com/')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]/div/ul/li[6]/div/div/div/a[1]').click()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="loginUsername"]').send_keys('13346647595')
# sleep(3)
# bb= dr.find_element_by_xpath('/html/body/ul').find_elements_by_tag_name('li')
# for i in bb:
#     # print(i)
#     if '@163.com' in i.text:
#         print(i.text)
#         i.click()
#         sleep(3)
#
# dr.find_element_by_xpath('//*[@id="loginPassword"]').send_keys('123456789')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="login"]').click()
# sleep(2)

































# dr.get('http://192.168.0.254/')
# sleep(5)
#
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# sleep(2)
#
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# sleep(2)
#
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# sleep(2)
#
#
# dr.find_element_by_xpath('//*[@id="input1"]').clear()
# sleep(2)
#
#
#
# # cc = dr.find_element_by_xpath('//*[@id="checkinfo"]').find_elements_by_xpath('img')
# for a in range(1,5):
#     cc = dr.find_element_by_xpath('//*[@id="checkinfo"]/img[{}]'.format(a))
#     bb = cc.get_attribute('src')
#     kk = re.compile(r'http://192.168.0.254/imgs/(.*?).gif')
#     oo = kk.findall(bb)
#     mm = oo[0]
#     dr.find_element_by_xpath('//*[@id="input1"]').send_keys(mm)
#     sleep(2)
#
#
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# sleep(5)
#
#
# wd = dr.switch_to_alert()      # 切换到弹出框
#
# # print(wd.text)               # 获取弹出框上的文本
# wd.accept()
# sleep(3)
#
# # dr.switch_to_alert()
# dr.switch_to.frame('left')
#
#
# dr.find_element_by_xpath('//*[@id="04"]').click()
# sleep(1)
#
# dr.find_element_by_xpath('//*[@id="041"]').click()
# sleep(1)
#
# dr.switch_to.default_content()
# dr.switch_to.frame('mainFrame')
#
# dr.find_element_by_xpath('//*[@id="content"]/form[2]/table/tbody/tr/td[2]/div/div/a').click()
# sleep(1)
# dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()
# sleep(5)




















# 弹出框(alert)

# wd = dr.switch_to_alert()      # 切换到弹出框
#
# print(wd.text)               # 获取弹出框上的文本
# wd.accept()                 # 点击确定
# # wd.dismiss()              #点击取消
# # wd.send_keys('内容')       # 向弹出框输入内容
# sleep(6)

















# dr.get('https://www.baidu.com/')
# sleep(3)
#
#
# dr.find_element_by_id('kw').send_keys('摩尔精英')
# sleep(1)
# dr.find_element_by_id('su').click()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="1"]/div[2]/a[1]').click()
# sleep(1)
#
# pp = dr.current_window_handle   #  获取当前窗口的句柄
# wd = dr.window_handles
#
# for i in wd:
#     if pp != i:
#         dr.switch_to.window(i)
#
#
#
# bb = dr.find_element_by_xpath('/html/body/div[2]/div/div[1]/div').find_elements_by_tag_name('div')
# for i in bb:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(3)






#
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
# sleep(3)

# oo = dr.current_window_handle   #  获取当前窗口的句柄
# lo = dr.window_handles
#
# for j in lo:
#     if oo != j:
#         dr.switch_to.window(j)
#
# dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('74110369')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('123456')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
# sleep(3)

















# dr.switch_to.frame('login')         # 切换到内嵌框架中，只能根据：id或者name或者 定位到框架 属性值来切换
# sleep(2)

# ww = dr.find_element_by_xpath('//*[@id="login_frame"]')
# dr.switch_to.frame(ww)
#
#
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('444205264')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('112233')
# sleep(2)
# # dr.find_element_by_xpath('//*[@id="login_button"]').click()
# # sleep(5)
#
#
#
# dr.switch_to.default_content()            ## 退出到原始的页面
#
# dr.find_element_by_xpath('//*[@id="lay"]/div[3]/div[1]/div[1]/ul/li[1]/a/span').click()
# sleep(2)



# dr.switch_to.parent_frame()            ## 切换到上一层框架  只能添加上一层id属性值，name属性值，定位到框架   来切换






















# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# sleep(1)
#
# pp = dr.current_window_handle   #  获取当前窗口的句柄
# wd = dr.window_handles            ## 获取所有句柄
#
#
# for i in wd:
#     if i != pp:
#         dr.switch_to.window(i)     ## 根据句柄 切换窗口
# # print(dr.title)
#
#
#
# dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('111222333')
# sleep(2)
#
# dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('112233')
# sleep(2)






















# dr.find_element_by_xpath('//*[@id="HD_CityName"]').send_keys('上海')
# sleep(1)
#
# dr.find_element_by_xpath('//*[@id="HD_CheckIn"]').clear()
# sleep(1)
#
# dr.find_element_by_xpath('//*[@id="HD_CheckOut"]').clear()
# sleep(1)
#
# bb = dr.find_element_by_xpath('//*[@id="J_roomCountList"]').find_elements_by_tag_name('option')
# for i in bb:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(3)




























# link_text  通过文本来定位，保证定位元素的唯一性
# dr.find_element_by_link_text('注册').click()
# # sleep(2)

# link_text =='文本'
# #partial_link_text in '文本'


# partial_link_text  通过模糊文本来定位，保证元素的唯一性
# dr.find_element_by_partial_link_text('注').click()
#
# sleep(2)


# 通过标签的名称去定位  通常用于多个元素的定位
# dr.find_element_by_tag_name().click()

## 通过xpath路径定位，  xpath：路径标记语言

# dr.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[3]/div[2]/div/span[1]/a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# sleep(3)

## 通过css selector 定位

# dr.find_element_by_css_selector('#user-nomal > div.login-wrap > div.before-login > li.no-register > a').click()
# sleep(3)


### 定位多个元素

## 定位多个class属性的值为 menu-box的元素   数据的类型是列表
## 层级定位
# bb= dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')
# bb = dr.find_elements_by_xpath('//*[@id="ttbar-login"]/a[1]')
# for i in bb:
    # ActionChains(dr).move_to_element(i).perform()
    # sleep(3)


# bb = dr.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]')
# print(bb.get_attribute('text'))        # 获取元素的某个属性的值

# bb = dr.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').text
# print(bb)











## 通过id属性定位  定位到id=kw 的位置
# dr.find_element_by_id('kw').send_keys('摩尔精英')
# sleep(3)
# dr.find_element_by_id('su').click()
# sleep(3)
# dr.find_element_by_class_name('c-showurl').click()
# sleep(5)


# dr.find_element_by_id('kw').send_keys('')
# sleep(5)
# dr.find_element_by_id('su').click()
# sleep(3)
















# dr.find_element_by_id('')





## 通过class属性定位，定位class=s_ipt的位置
# dr.find_element_by_class_name('s_ipt').send_keys('美女')
# sleep(3)

# sleep(5)

## 通过name属性定位  定位到  name=wd的位置

# dr.find_element_by_name('wd').send_keys('美女')
# sleep(3)
# dr.find_element_by_id('su').click()
# sleep(3)















# 获取网站的标题（title）

# print(dr.title)   #通常用来做断言的
#
# # 获取网站的网址
#
# print(dr.current_url)
#
#
# ##保证所有的测试用例在同一环境下测试
#
#
# # 设置浏览器的大小
#
# dr.set_window_size(1500,1500)        # 第一个是宽，第二个是高
# sleep(2)
#
# #  设置浏览器的位置
# dr.set_window_position(500,500)     # 第一个是x轴，第二个是y轴
# sleep(2)
#
#
# dr.maximize_window()   ##浏览器最大化
# sleep(2)
#
# # dr.minimize_window()   ##浏览器最小化
# # sleep(3)
#
# dr.get('https://www.jd.com')
# sleep(3)
#
# dr.back()             ## 后退
# sleep(2)
#
# dr.forward()          ## 前进
# sleep(2)















dr.quit()            # 关闭浏览器


