# coding=UTF-8
import os

from selenium import webdriver
import time

from driver.wait import Wait
from selenium.webdriver import ActionChains

from page.BasePage import BasePage,BaseHandler


class test:
    def login(self):
        # #登录
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        # self.driver.get('http://114.115.205.214:8686/Ecan_Platform/loginAction!login_page.action')
        # self.driver.find_element_by_xpath('//*[@id="userid"]').send_keys('00')
        # self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('1')
        # self.driver.find_element_by_xpath('//*[@id="loginButton"]').click()
        # return self.driver

        # #搜索双击进入菜单表单
        # self.driver.find_element_by_xpath('//*[@id="dept_id_2"]').send_keys('入库单审核')
        # ac = ActionChains(self.driver)
        # ac.double_click(self.driver.find_element_by_xpath('//*[@id="ext-gen123"]/div')).perform()
        # time.sleep(8)
        #
        # self.driver.switch_to.frame('iframe15130802')



        #输入查询数据点击查询，联合BasePage初始化进行测试
        # wait = WebDriverWait(self.driver, 10, 0.5)
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="begin_str_change_id"]'))).send_keys('RK202012001')
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="end_str_change_id"]'))).send_keys('RK202012001')
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ext-gen40"]'))).click()
        wait = BasePage()
        self.driver = wait.driver
        self.driver.find_element_by_xpath('//*[@id="dept_id_2"]').send_keys('入库单审核')
        time.sleep(1)
        ac = ActionChains(self.driver)
        ac.double_click(self.driver.find_element_by_xpath('//*[@id="ext-gen123"]/div')).perform()
        self.driver.switch_to.frame('iframe15130802')
        handler = BaseHandler()
        handler.input_text(wait.Find(('xpath','//*[@id="begin_str_change_id"]')),'RK202012001')
        handler.input_text(wait.Find(('xpath','//*[@id="end_str_change_id"]')),'RK202012001')
        handler.click(wait.Find(('xpath','//*[@id="ext-gen40"]')))
        self.driver.quit()


    def set_case_list(self):
        """设置case
        set case list
        :return:
        """
        self.caseList = []
        self.caseListFile = os.path.join(os.getcwd(), "caselist.txt")
        fb = open(self.caseListFile,encoding='utf-8')                #打开case
        for value in fb.readlines():                #读取case数据
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()
        print(self.caseList)

if __name__ == '__main__':
    test().login()
    # time.sleep(8)
    # test().set_case_list()
