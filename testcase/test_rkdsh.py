# coding=UTF-8

import pytest
import allure
import yaml
import os

from driver.login import Login
from driver.Log import MyLog
from page.Rkdsh_Page import RkdshService
from testFile.data.rkdsh_data import rkdsh_data_queryis

cur_path = os.path.dirname(os.path.realpath(__file__))  #打开yaml文件
yaml1 = os.path.join(cur_path, '../testFile/data/rkdsh_data.yml')
yaml_data = yaml.load(open(yaml1), Loader=yaml.FullLoader)  # 使用load方法加载yml问价

@allure.testcase("入库单审核查询功能的testcase",name="testcase_link")#testcase、link、issue会出现在测试报告的link
@allure.feature("入库单审核查询功能测试feature")          #也可以根据功能名执行测试用例
@allure.severity(allure.severity_level.CRITICAL)    #重要程度，到时候可以根据重要程度筛选执行测试用例
class Test_rkdsh():
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


    @pytest.mark.run(order=1)   #测试用例执行顺序，在有需要的时候再用，还有其他使用方法具体用到再看
    @allure.story("根据存在单据号查询入库单")
    @pytest.mark.parametrize("test_info", rkdsh_data_queryis)#这个会出现在测试报告的Parameters中,这里数据驱动数据存在py文件中
    def test_demo1(self,test_info):
        '''
        根据单据查询      这个信息会出现在测试报告的Description中，相当于@allure.description
        '''
        self.driver.refresh()   #每次要刷新一下，进行页面清洗，因为执行多个测试用例要保证开始的页面是干净的
        self.logger.info("根据存在单据号查询入库单")
        with allure.step('测试步骤 输入两个单号后点击查询'):
            allure.attach('输入第一个单号')
            allure.attach('输入第二个单号')
            allure.attach('点击查询按钮')
        self.rkdsh_service.query(test_info[0],test_info[1])

    @pytest.mark.run(order=2)
    @allure.story("根据不存在单据号查询入库单")
    # @pytest.mark.parametrize("test_info", [['RK202012004','RK202012004']])
    @pytest.mark.parametrize("test_info", yaml_data['rkdsh_data_querynull'])#这里使用数据驱动数据存在yml文件中
    def test_demo2(self,test_info):
        '''
        根据单据查询
        '''
        self.driver.refresh()
        self.logger.info("根据不存在单据号查询入库单")
        with allure.step('测试步骤 输入两个单号后点击查询'):
            allure.attach('输入第一个单号')
            allure.attach('输入第二个单号')
            allure.attach('点击查询按钮')
        self.rkdsh_service.query(test_info[0],test_info[1])

    @pytest.mark.run(order=3)
    @allure.story('allure.story 第三个子功能')
    def test_demo3(self):
        print('test_1')

    @pytest.mark.run(order=4)
    @pytest.mark.skipif(reason='本次不执行')
    @allure.story('allure.story 第四个子功能')
    def test_demo4(self):
        print('测试本次不执行')

if __name__ == '__main__':
    # pytest.main(['test_rkdsh.py'])

    #要在控制台中执行，这个可以右键run file in python console
    pytest.main(['-s','-q','--alluredir=./report/tmp','--clean-alluredir','test_rkdsh.py'])
    # os.system('allure generate ./report/tmp -o ./report/report --clean')