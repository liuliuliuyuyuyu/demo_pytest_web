# coding=UTF-8
#等待对象模块
from selenium.webdriver.support import expected_conditions as EC
#等待条件模块
from selenium.webdriver.support.wait import WebDriverWait
#查询元素模块
from selenium.webdriver.common.by import By

#现在弃用了，已经封装到BasePage中了
class Wait():
    def __init__(self,driver):
        self.wa = WebDriverWait(driver, 20, 0.5)
    def waitSend(self,location,value):
        self.wa.until(EC.visibility_of_element_located(location)).send_keys(value)
    def waitClick(self,location):
        self.wa.until(EC.visibility_of_element_located(location)).click()
    def waitFind(self,location):
        return self.wa.until(EC.visibility_of_element_located(location))


