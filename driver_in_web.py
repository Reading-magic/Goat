from selenium import webdriver
import time

dr = webdriver.Firefox(executable_path='F:\Mozilla Firefox\geckodriver.exe')#启动geckodriver
time.sleep(5)#停止5秒钟
print('Brower will close')
dr.quit#关闭
print('Browser is close')


#会弹出黑色窗口。还需要改进
