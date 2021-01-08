# coding=UTF-8
import pytest
from driver.Log import Log, MyLog
from driver.driver import Driver


class Run:
    def __init__(self):
        log = MyLog.get_log()    #注意这里要使用MyLog中的线程锁，否则log日志会重复
        self.logger = log.get_logger

    def run(self):
        Driver.is_open = False      #打开浏览器开关
        self.logger.info("********TEST START********")
        # 运行某个模块内某个类的某个测试方法：文件名::类名::测试用例名
        # pytest.main(['test_rk.py'])
        # 执行某个目录下的所有测试
        pytest.main(['testcase/'])
        run.logger.info("*********TEST END*********")
        Driver.is_open = True       #关闭浏览器开关
        Driver.quit_dirver()        #关闭浏览器


if __name__ == '__main__':
    run = Run()
    run.run()
