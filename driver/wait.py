#等待对象模块
from selenium.webdriver.support import expected_conditions as EC
#等待条件模块
from selenium.webdriver.support.wait import WebDriverWait
#查询元素模块
from selenium.webdriver.common.by import By


class Wait():
    def __init__(self,driver):
        print("111111111111111111")
        self.wa = WebDriverWait(driver, 10, 0.5)
    def waitSend(self,type,route,value):
        if type == 'xpath':
            self.wa.until(EC.visibility_of_element_located((By.XPATH, route))).send_keys(value)
    def waitClick(self,type,route):
        if type == 'xpath':
            self.wa.until(EC.visibility_of_element_located((By.XPATH, route))).click()
    def waitFind(self,type,route):
        if type == 'xpath':
            self.wa.until(EC.visibility_of_element_located((By.XPATH, route)))
