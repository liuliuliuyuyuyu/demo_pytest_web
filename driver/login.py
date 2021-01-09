# coding=UTF-8
from selenium import webdriver
import time

#等待对象模块
from selenium.webdriver.support import expected_conditions as EC
#等待条件模块
from selenium.webdriver.support.wait import WebDriverWait
#查询元素模块
from selenium.webdriver.common.by import By

class Login:
    _driver = None    #使用私有变量防止修改
    is_open = True      #浏览器驱动启动开关

    #使用类方法，判断浏览器驱动是否已经启动，若启动直接返回启动的驱动，未启动则会开启，保证了在单个python测试文件中的浏览器驱动唯一
    @classmethod
    def login(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.get('http://114.115.205.214:8686/Ecan_Platform/loginAction!login_page.action')
            wait = WebDriverWait(cls._driver, 20, 0.5)
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="userid"]'))).send_keys('00')
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="password"]'))).send_keys('1')
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="loginButton"]'))).click()

            #当确认登录成功，页面出现登录成功元素再返回
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="west-panel"]')))
        return cls._driver

    # 关闭浏览器驱动，通过if判断是否关闭，如果没有关闭帮忙关闭，并且进行初始化
    @classmethod
    def quit_dirver(cls):
        if cls.is_open and cls._driver is not None:
            cls.login().quit()
            cls._driver = None


if __name__ == '__main__':
    Login().login()
    time.sleep(8)