import time

from page.BasePage import BasePage
from driver.wait import Wait


class RkdshPage(BasePage):
    def __init__(self,driver):
        #调用父类BasePage的__init__方法，相当于java中的重载,super() 函数是用于调用父类(超类)的一个方法。
        super().__init__(driver)
        self.driver.switch_to.frame('iframe15130802')
    def query(self, value1, value2):
        wait = Wait(self.driver)
        wait.waitSend('xpath', '//*[@id="begin_str_change_id"]', value1)
        wait.waitSend('xpath', '//*[@id="end_str_change_id"]', value2)
        wait.waitClick('xpath', '//*[@id="ext-gen40"]')

        return self


