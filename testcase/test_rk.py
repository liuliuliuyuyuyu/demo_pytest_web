# coding=UTF-8

import pytest

from driver.login import Login
from driver.Log import Log, MyLog
from page.MainPage import MainPage
from page.RkdshPage import RkdshPage


class Testrk():
    def setup_class(self):
        log = MyLog.get_log()
        self.logger = log.get_logger
        self.logger.info("测试开始")
    def setup_method(self):
        self.driver = Login().login()
        self.main = MainPage(self.driver)

    def test_demo(self):
        self.logger.info("入库单审核查询")
        self.main.search(keyword="入库单审核")
        RkdshPage(self.driver).query('RK202012001','RK202012001')


    def test_demo2(self):
        self.logger.info("出库单审核查询")
        self.main.search(keyword="出库单审核")

    def teardown_method(self):
        self.driver.quit()
    def teardown_class(self):
        self.logger.info("测试结束")

if __name__ == '__main__':
    pytest.main(['test_rk.py'])