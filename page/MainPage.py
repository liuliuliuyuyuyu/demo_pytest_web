# coding=UTF-8

from page.BasePage import BasePage,BaseHandler

#通过主页的搜索菜单打开各页面，现在也展示启用，直接在测试用例中使用self.driver.get(url)进入
class MainPage(BasePage):
    def search(self,keyword):
        # baseHandler = BaseHandler(self.driver)
        baseHandler = BaseHandler()
        baseHandler.input_text(self.Find(('xpath', '//*[@id="dept_id_2"]')), keyword)
        MainPage.Find(('xpath', '//*[@id="ext-gen123"]/div'))

        BaseHandler.double_click(('xpath','//*[@id="ext-gen123"]/div'))
        # ac = ActionChains(self.driver)
        # ac.double_click(self.driver.find_element_by_xpath('//*[@id="ext-gen123"]/div')).perform()
        return self



