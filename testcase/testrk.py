import time

import pytest

from driver.login import Login
from page.MainPage import MainPage
from page.RkdshPage import RkdshPage

class Testrk():
    def setup(self):
        self.driver = Login().login()
        self.main = MainPage(self.driver)

    def test_demo(self):
        self.main.search(keyword="入库单审核")
        RkdshPage(self.driver).query('RK202012001','RK202012001')


    def test_demo2(self):
        self.main.search(keyword="出库单审核")


    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['testrk.py'])