# coding=UTF-8
import pytest

from driver.login import Login
from driver.Log import MyLog


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
        pytest.main(['testcase/'])  #执行测试
        run.logger.info("*********TEST END*********")
        Login.is_open = True    #关闭浏览器驱动开关
        Login.quit_dirver()     #最后如果浏览器没有关闭这里就再关闭一下


if __name__ == '__main__':
    run = Run()
    run.run()
