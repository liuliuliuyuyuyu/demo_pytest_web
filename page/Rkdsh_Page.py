# coding=UTF-8

from page.BasePage import BasePage,BaseHandler

'''
注意
    每一层只做自己层的事情
    业务层获取操作层方法进行业务逻辑执行
    操作层获取对象层对象进行单个步骤操作
    对象层就获取功能模块上的元素就行
'''

'''所有功能模块的对象层都继承与BasePage的对象层'''
#三层模型封装：对象层
class RkdshPage(BasePage):
    def __init__(self): #重写__init__方法
        # 调用父类BasePage的__init__方法，相当于java中的重载,super() 函数是用于调用父类(超类)的一个方法。
        super().__init__()  #重写继承回父类的__init__方法，继承了__init__中的属性

    '''每个功能模块对象层对象不一样，每个方法对应一个对象，但是方法中获取对象的操作方法是一致的，都已经封装到BasePage中了'''
    #获取单号1输入框
    def find_danhao1(self):
        #使用BasePage封装好的方法进行元素的查找
       return  self.Find(('xpath', '//*[@id="begin_str_change_id"]'))

   #获取单号2输入框
    def find_danhao2(self):
       return self.Find(('xpath', '//*[@id="end_str_change_id"]'))

   # 获取查询按钮
    def find_chaxun(self):
       return self.Find(('xpath', '//*[@id="ext-gen40"]'))



'''所有功能模块的操作层都继承与BasePage的操作层'''
#三层模型封装：操作层
class RkdshHandler(BaseHandler):
    def __init__(self):
        self.Rkdsh_page = RkdshPage()   #先要初始化获取对象层，再对对象层中的对象进行操作

    '''每个功能模块操作层的操作都不一样，每个方法对应一个操作，但是方法中获取操作的操作方法是一致的，都已经封装到BaseHandler中了
    操作的元素使用在对象层中获取的对象'''
    #在单号1输入框输入单号
    def input_danhao1(self, value):
        #使用BaseHandler中封装好的方法进行元素的操作
        self.input_text(self.Rkdsh_page.find_danhao1(),value)
    # 在单号2输入框输入单号
    def input_danhao2(self, value):
        self.input_text(self.Rkdsh_page.find_danhao2(),value)
    # 点击查询按钮
    def click_chaxun(self):
        self.click(self.Rkdsh_page.find_chaxun())


'''业务层为每个功能模块的具体实现'''
#三层模型封装：业务层
class RkdshService:
    def __init__(self):
        self.Rkdsh_handler = RkdshHandler() #先初始化操作层

    #把操作层的单个操作根据功能组成不同的业务逻辑执行
    def query(self, value1, value2):
        #完整的查询操作
        self.Rkdsh_handler.input_danhao1(value1)
        self.Rkdsh_handler.input_danhao2(value2)
        self.Rkdsh_handler.click_chaxun()

