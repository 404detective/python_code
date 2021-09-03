from selenium import webdriver
import time
import re

def open_browser():
    browser = webdriver.Chrome()               

    browser.get('https://blink.csdn.net/?username=qq_26230027')   


    for i in range(20):
        print('测试点赞第%d次'%i)
    pass
    time.sleep(30)
    for i in range(2000):
        browser.find_element_by_xpath("//div[@class='b-i-btn agree']").click()
        time.sleep(5)
        print('点赞第%d次'%i)
    
    time.sleep(20000)

pass

open_browser()

# <div data-v-315887f8="" class="b-i-btn agree"><span data-v-315887f8="">29</span></div>
#<span data-v-315887f8="">40</span>