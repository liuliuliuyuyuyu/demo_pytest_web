# 基类文件
import random
import time


import win32con
import win32gui
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver.driver import Driver


'''创建对象库层的基类'''
class BasePage():

    def __init__(self):
        self.driver = Driver.get_driver()
    #用于单个元素定位
    def find_ele(self,location):
        print(location)
        return self.driver.find_element(*location)

    #用于元素数组定位
    def find_eles(self, location):
        print(location)
        return self.driver.find_elements(*location)
    #元素是否被加载dom
    def find_wait_p(self, location):
        return  WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(location))
        # try:
        #     ele=WebDriverWait(self.driver,20).until(EC.presence_of_element_located(location))
        #     print(location)
        # except TimeoutException as e:
        #     print("{}该元素查找超时".format(location))
        #     raise e
        # else:
        #     return ele

    #元素可见
    def find_wait_v(self,location):
        # return self.driver.find_elements(*location)
        # ele1 = WebDriverWait(self.driver, 5, 0.2).until(EC.presence_of_all_elements_located())
        # return ele1
        try:
            ele1=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(location))
            print(location)
        except TimeoutException as e:
            print("{}该元素不可见".format(location))
            raise e

        # return self.driver.find_element(*location)
        else:
            return ele1
    #元素可点击
    def find_wait_c(self,location):
        try:
            ele=WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(location))
            print(location)
        except TimeoutError as e:
            print("{}该元素不可点击".format(location))
            raise e
        else:
            return ele


'''创建操作层的基类'''
class BaseHandler():
    def text(self,element):
        return  element.text
    # 输入文本
    def input_text(self, element, text):
        print("{}输入{}成功".format(element,text))
        element.send_keys(text)
    #js点击按钮
    def js_click(self,element):
        # Driver.get_driver().find_element(element).click()
        #
        try:
            print("{}JS点击按钮成功".format(element))
            Driver.get_driver().execute_script("arguments[0].click();", element)
        # webdriver.ActionChains(Driver.get_driver()).click(element).perform()
        except Exception as e:
            print(e,"{}JS点击按钮失败".format(element))

         #鼠标点击按钮
    def click(self, element):
        # webdriver.ActionChains(Driver.get_driver()).click(element).perform()
        try:
            print("{}鼠标点击按钮成功".format(element))
            webdriver.ActionChains(Driver.get_driver()).move_to_element(element).click(element).perform()

        except Exception as e:
            print(e,"{}鼠标点击按钮失败".format(element))


    #iframe转换
    def cutin_text_iframe(self,element):
        #切入
        Driver.get_driver().switch_to.frame(element)
    def cutout_text_iframe(self):
        #切出
        Driver.get_driver().switch_to.default_content()

    #文件上传
    def file_upload(self,route):
        dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        time.sleep(1.5)
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, route)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

    #日期框变为可输入
    def date_input(self,style,ele,index):
        """

        :param style: CSS元素类型
        :param ele: CSS元素
        :param index: 下标
        :return:
        """
        self.js='document.getElementsBy{}("{}")[{}].removeAttribute("readonly")'.format(style,ele,index)
        Driver.get_driver().execute_script(self.js)
     #内嵌滚动条
    def scroll(self,ele):
        Driver.get_driver().execute_script("arguments[0].scrollIntoView();",ele)
    # def a(self):
    #     ele=Driver.get_driver().find_element_by_xpath("//div[@title='{}']".format(BaseHandler().ra))
    #     return ele.text
    def js(self,ele):
        Driver.get_driver().execute_script(ele)

    # ele = Driver.get_driver().find_element_by_xpath("//div[@title='立项测试{}']".format(ra)).text