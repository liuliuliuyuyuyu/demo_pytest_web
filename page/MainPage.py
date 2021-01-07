# coding=UTF-8
import time

from selenium.webdriver import ActionChains

from driver.wait import Wait
from page.BasePage import BasePage


class MainPage(BasePage):
    def search(self,keyword):
        wait = Wait(self.driver)
        wait.waitSend('xpath', '//*[@id="dept_id_2"]', keyword)
        wait.waitFind('xpath', '//*[@id="ext-gen123"]/div')

        # self.driver.find_element_by_xpath('//*[@id="dept_id_2"]').send_keys(keyword)
        ac = ActionChains(self.driver)
        ac.double_click(self.driver.find_element_by_xpath('//*[@id="ext-gen123"]/div')).perform()
        return self



