# coding=UTF-8

import pytest
import allure

from driver.login import Login
from driver.Log import MyLog
from page.Rkdsh_Page import RkdshService


@allure.feature("入库单审核查询功能测试")
class Testrk():
    @classmethod
    def setup_class(self):
        log = MyLog.get_log()
        self.logger = log.get_logger
        self.logger.info("测试开始")
        self.driver = Login().login()
    def setup_method(self):
        self.driver.get('http://114.115.205.214:8686//E_Gdzc_3/gdzc/inputAction!listNeedCheck.action')
        self.rkdsh_service = RkdshService()

    @classmethod
    def teardown_class(self):
        self.driver.quit()
        self.logger.info("测试结束")

    @pytest.mark.parametrize("test_info", [['RK202012001','RK202012001']])
    @pytest.mark.run(order=1)
    @allure.story("根据单据号查询入库单")
    def test_demo(self,test_info):
        '''
        根据单据查询
        '''
        self.logger.info("入库单审核查询1")
        self.rkdsh_service.query(test_info[0],test_info[1])

    @pytest.mark.parametrize("test_info", [['RK202012002','RK202012002']])
    @pytest.mark.run(order=2)
    @allure.story("根据单据号查询入库单")
    def test_demo2(self,test_info):
        '''
        根据单据查询
        '''
        self.logger.info("入库单审核查询2")
        self.rkdsh_service.query(test_info[0],test_info[1])

if __name__ == '__main__':
    pytest.main(['test_rkdsh.py'])