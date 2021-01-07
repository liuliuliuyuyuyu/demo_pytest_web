# coding=UTF-8

import os
import logging
from datetime import datetime
import threading

#输出日志

class Log(object):
    def __init__(self):
        proDir = os.getcwd()     #os.getcwd()表示当前路径，"../.."表示上上级路径
        # proDir = os.path.abspath(os.path.join(os.getcwd(), "..")) # 上级路径
        resultPath = os.path.join(proDir, "result")   #结果文件夹result路径
        if not os.path.exists(resultPath):            #判断文件夹是否存在，如果存在
            os.mkdir(resultPath)                       #如果没有就创建
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M")))    #拼接log文档生成的文件夹名以%Y%m%d%H%M%S格式
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # 如果不想别人修改log，可以先变为私有变量
        self._logger = logging.getLogger('gdzc')              #使用接口调试，信息，警告，错误，严重之前必须创建记录器实例,设置实例名gdzc
        self._logger.setLevel(logging.INFO)             #设置日志级别
                                                        # CRITICAL: 'CRITICAL',
                                                        # ERROR: 'ERROR',
                                                        # WARNING: 'WARNING',
                                                        # INFO: 'INFO',
                                                        # DEBUG: 'DEBUG',
                                                        # NOTSET: 'NOTSET',

        # defined handler                       Handler处理器，将（记录器产生的）日志记录发送至合适的目的地，可以修改日志文件的编码格式
        handler = logging.FileHandler(os.path.join(logPath, "result.log"),encoding='utf-8')
        # defined formatter                     格式化器，指明了最终输出中日志记录的布局   使用Formatter对象设置日志信息最后的规则，结构和内容，默认的时间格式为％Y-％m-％d％H：％M：％S
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)        #格式化，给handler选择一个Formatter
        self._logger.addHandler(handler)        #为logger添加句柄

    '''这里用到了property装饰器，可以把方法变成属性，原本方法调用需要get_logger(),现在只要get_logger就可以'''
    @property
    def get_logger(self):
        """获取记录
        get logger
        :return:
        """
        return self._logger

    def build_start_line(self, case_no):
        """写入起始行
        write start line
        :return:
        """
        self._logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """写入结束行
        write end line
        :return:
        """
        self._logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name):
        """编写测试用例行
        write test case line
        :param case_name:
        :param code:
        :return:
        """
        self._logger.info(case_name)


class MyLog:                    #放进线程组内
    log = None
    mutex = threading.Lock()    #线程锁一次只能一个锁定

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()      #线程调用acquire方法获得锁，锁进入locked状态。     因为每次只有一个线程1可以获得锁，所以如果此时另一个线程2试图获得这个锁，该线程2就会变为“block“同步阻塞状态。直到拥有锁的线程1调用锁的release()方法释放锁之后，该锁进入“unlocked”状态。线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态。
            MyLog.log = Log()          #启动Log初始化
            MyLog.mutex.release()

        return MyLog.log

if __name__ == "__main__":
    logger = Log().get_logger    #获取记录
    logger.debug("test debug")  #测试级别为bug
    logger.info("test info")    #测试级别为info

