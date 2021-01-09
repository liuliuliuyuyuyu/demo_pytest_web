# coding=UTF-8

import logging

#这个也已经废弃了使用Log了
class BaseTestCase(object):
    logging.basicConfig()  # 先初始化
    # 设置一个独立的log，在为它设置级别
    #如果不想别人修改log，可以先变为私有变量
    _log = logging.getLogger('gdzc')
    _log.setLevel(logging.INFO)

    #在调用方法获取变量
    '''这里用到了property装饰器，可以把方法变成属性，原本方法调用需要log(),现在只要log就可以'''
    @property
    def log(self):
        return self._log
