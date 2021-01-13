# coding=UTF-8
import pytest

from driver.login import Login
from driver.Log import MyLog
from result.report.configEmail import MyEmail


class Run:
    def __init__(self):
        log = MyLog.get_log()    #注意这里要使用MyLog中的线程锁，否则log日志会重复
        self.logger = log.get_logger


    def run(self):
        Login.is_open = False   #打开浏览器驱动开关
        self.logger.info("********TEST START********")
        # 运行某个模块内某个类的某个测试方法：文件名::类名::测试用例名
        # pytest.main(['test_rkdsh.py'])
        # 执行某个目录下的所有测试
        # pytest.main(['testcase/'])  #执行测试

        # pytest.main(['-s','test_allure.py::TestAllure::test_allure'])
        '''在测试期间收集结果  把结果保存到result文件夹里，如果没有这个文件夹就先创建文件夹,先清除之前的生成结果'''
        pytest.main(['-s','-q','--alluredir=./result/report/tmp','--clean-alluredir','testcase/'])
        '''控制台中运行 拿结果生成报告，是一个启动tomcat的服务，只生成报告 覆盖路径加--clean清除之前的报告    在report文件夹中生成报告'''
        # os.system('allure generate ./result/report/tmp -o ./result/report/report --clean')
        '''按功能模块执行'''
        # pytest.main(["--allure_feature='allure.feature 测试allure' --allure_stories='allure.story 测试第一个子功能'"])
        '''按重要性测试'''
        # pytest.main(['-s','-v','test_allure.py','--allure-severities=normal,critical'])

        self.logger.info("*********TEST END*********")
        Login.is_open = True    #关闭浏览器驱动开关
        Login.quit_dirver()     #最后如果浏览器没有关闭这里就再关闭一下

        #发送邮件，自己选择发不发
        # self.logger.info("**********发送邮件**********")
        # email = MyEmail.get_email()
        # email.send_email()



if __name__ == '__main__':
    #右键run file in python console执行
    run = Run()
    run.run()
