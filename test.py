import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
# from selenium.webdriver.edge.options import Options
# from
resp=urlopen('http://172.19.1.9:8080/')                                            #xxxxx为网址 具体看校园网页面情况
code=resp.getcode()
if code==200:                                                            #验证网址是否正常
    f=open('UserNK.txt')                                                 #读取记事本，这里可以自己改名
    user_name,user_key=f.read().splitlines()                             #按行读取并赋值账户和密码
    f.close() #关闭记事本
    driver=webdriver.Edge(r'msedgedriver.exe') #驱动所在的路径
    driver.get("http://172.19.1.9:8080/")  # 网址
    driver.maximize_window()  # 窗口最大化
    time.sleep(3)  # 等待1秒
    driver.find_element_by_id("username").click()  # 模拟点击账户输入框（id可以右键检查看到）
    driver.find_element_by_id("username").send_keys(user_name)  # 输入账户名
    driver.find_element_by_id("username").send_keys(Keys.TAB)  # 切换至密码框
    driver.find_element_by_id("pwd").send_keys(user_key)  # 输入密码
    driver.find_element_by_id("pwd").send_keys(Keys.ENTER)  # 模拟按下回车
    driver.find_element_by_id("xiala").click()
    driver.find_element_by_id("_service_3").click()
    driver.find_element_by_class_name("disPlayIs_check").click()
    driver.find_element_by_id("loginLink_div").click()
    driver.quit()  # 关闭页面
else:  # 网址无效则
    sys.exit()  # 程序终止运行