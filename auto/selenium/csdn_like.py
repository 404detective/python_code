from selenium import webdriver
import time
import re
from pyquery import PyQuery as pq

def open_browser():
    browser = webdriver.Chrome()                 #创建浏览器
# opt.set_headless()                            #无窗口模式
    browser.get('https://blink.csdn.net/?username=qq_26230027')   #打开网页
# driver.maximize_window()                      #最大化窗口
    #html=browser.page_source

    for i in range(20):
        print('测试点赞第%d次'%i)
    pass
    time.sleep(60)
    for i in range(2000):
        browser.find_element_by_xpath("//span[@class='b-i-btn agree']").click()
        time.sleep(10)
        print('点赞第%d次'%i)
    
    time.sleep(20000)

pass

open_browser()

# <div data-v-315887f8="" class="b-i-btn agree"><span data-v-315887f8="">29</span></div>
#<span data-v-315887f8="">40</span>
