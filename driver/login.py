# coding=UTF-8
from selenium import webdriver
import time

from driver.wait import Wait


class Login:
    def login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://114.115.205.214:8686/Ecan_Platform/loginAction!login_page.action')
        wait = Wait(self.driver)
        wait.waitSend('xpath', '//*[@id="userid"]', '00')
        wait.waitSend('xpath', '//*[@id="password"]', '1')
        wait.waitClick('xpath', '//*[@id="loginButton"]')

        # self.driver.find_element_by_xpath('//*[@id="userid"]').send_keys('00')
        # self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('1')
        # self.driver.find_element_by_xpath('//*[@id="loginButton"]').click()
        return self.driver

if __name__ == '__main__':
    Login().login()
    time.sleep(8)