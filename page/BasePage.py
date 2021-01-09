# coding=UTF-8
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
#等待对象模块
from selenium.webdriver.support import expected_conditions as EC
#等待条件模块
from selenium.webdriver.support.wait import WebDriverWait
#查询元素模块
from selenium.webdriver.common.by import By

from driver.Driver import Driver
from driver.login import Login


#创建对象层
class BasePage():
    def __init__(self):
        #获取浏览器驱动，如果已经启动返回已经启动的驱动
        self.driver:WebDriver = Login.login()
        self.wa = WebDriverWait(self.driver, 20, 0.5)

    #显示等待定位元素,元素可见：visibility_of_element_located
    def Find(self,location):
        return self.wa.until(EC.visibility_of_element_located(location))

    # 显示等待定位元素数组
    def Finds(self,location):
        return self.wa.until(EC.visibility_of_all_elements_located(location))

    # 元素是否被加载dom，元素被加载：presence_of_element_located
    def find_wait_p(self,location):
        return self.wa.until(EC.presence_of_element_located(location))

    # 元素可点击：presence_of_element_located，这里也可以使用异常处理，随便自己
    def find_wait_c(self,location):
        try:
            ele = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(location))
            print(location)
        except TimeoutError as e:
            print("{}该元素不可点击".format(location))
            raise e
        else:
            return ele

#创建操作层
class BaseHandler():
    #返回文本内容
    def text(self,element):
        return element.text
    #输入文本
    def input_text(self,element,value):
        print("{}输入{}成功".format(element, value))
        element.send_keys(value)
    #点击按钮
    def click(self,element):
        element.click()

    # js点击按钮
    def js_click(self, element):
        # DriverUtil.get_driver().find_element(element).click()
        #
        try:
            print("{}JS点击按钮成功".format(element))
            Driver.get_driver().execute_script("arguments[0].click();", element)
        # webdriver.ActionChains(DriverUtil.get_driver()).click(element).perform()
        except Exception as e:
            print(e, "{}JS点击按钮失败".format(element))

    # action点击按钮
    def action_click(self, element):
        # webdriver.ActionChains(DriverUtil.get_driver()).click(element).perform()
        try:
            print("{}鼠标点击按钮成功".format(element))
            ActionChains.click(element).perform()
        except Exception as e:
            print(e, "{}鼠标点击按钮失败".format(element))

    # action双击按钮
    def double_click(self, element):
        # webdriver.ActionChains(DriverUtil.get_driver()).click(element).perform()
        try:
            print("{}鼠标点击按钮成功".format(element))
            ActionChains.double_click(element).perform()
        except Exception as e:
            print(e, "{}鼠标点击按钮失败".format(element))

    # iframe表单切换
    def enter_text_iframe(self, iframeid):
        # 切入
        Driver.get_driver().switch_to.frame(iframeid)

    def out_text_iframe(self):
        # 切出
        Driver.get_driver().switch_to.default_content()

    # 文件上传
    def file_upload(self, route):
        pass
        # dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        # Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        # button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        # time.sleep(1.5)
        # win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, route)  # 往输入框输入绝对地址
        # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

    # 日期框变为可输入
    def date_input(self, style, ele, index):
        """

        :param style: CSS元素类型
        :param ele: CSS元素
        :param index: 下标
        :return:
        """
        self.js = 'document.getElementsBy{}("{}")[{}].removeAttribute("readonly")'.format(style, ele, index)
        Driver.get_driver().execute_script(self.js)

    # 内嵌滚动条
    def scroll(self, ele):
        Driver.get_driver().execute_script("arguments[0].scrollIntoView();", ele)

    # def a(self):
    #     ele=DriverUtil.get_driver().find_element_by_xpath("//div[@title='{}']".format(BaseHandler().ra))
    #     return ele.text
    def js(self, ele):
        Driver.get_driver().execute_script(ele)

    # ele = DriverUtil.get_driver().find_element_by_xpath("//div[@title='立项测试{}']".format(ra)).text





