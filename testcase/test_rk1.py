# coding=UTF-8

import pytest
import allure

from driver.login import Login
from driver.Log import Log, MyLog
from page.MainPage import MainPage
from page.Rkdsh_Page import RkdshPage


@allure.feature("入库单审核查询功能测试")
class Testrk():
    @classmethod
    def setup_class(self):
        log = MyLog.get_log()
        self.logger = log.get_logger
        self.logger.info("测试开始")
    def setup_method(self):
        self.driver = Login().login()
        self.main = MainPage(self.driver)

    @pytest.mark.parametrize("test_info", [['RK202012001','RK202012001']])
    @pytest.mark.run(order=1)
    @allure.story("根据单据号查询入库单")
    def test_demo(self,test_info):
        '''
        根据单据查询
        '''
        self.logger.info("入库单审核查询")
        self.main.search(keyword="入库单审核")
        RkdshPage(self.driver).query(test_info[0],test_info[1])

    @pytest.mark.parametrize("test_info", [['RK202012001','RK202012001']])
    @pytest.mark.run(order=2)
    @allure.story("根据单据号查询出库单")
    def test_demo2(self,test_info):
        '''
        根据单据查询
        '''
        self.logger.info("出库单审核查询")
        self.main.search(keyword="出库单审核")
        print(test_info)

    def teardown_method(self):
        self.driver.quit()

    @classmethod
    def teardown_class(self):
        self.logger.info("测试结束")

if __name__ == '__main__':
    pytest.main(['test_rk1.py'])