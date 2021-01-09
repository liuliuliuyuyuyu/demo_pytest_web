class A:
    member = "this is a A."
    def __init__(self):
        pass
    @classmethod
    def Print1(cls):
        print("print 1: ", cls.member)
        print(cls().Print2())#不管是使用A.Print1调用还是A().Print1调用，这里都必须写成cls().Print2
        # a = A()
        # A.Print1()和 a.Print1()，结果都为：print 1:  this is a test.
    def Print2(self):
        print("print 2: ", self.member)
        # a = A()
        # A.Print2()：报错因为没有实例无法访问， a.Print2()：print 2:  this is a test.
    @classmethod
    def Print3(paraTest):
        print("print 3: ", paraTest.member)
        # a = A()
        # A.Print3()和 a.Print3，结果都为：print 3:  this is a test.
    @staticmethod
    def Print4():
        print("hello")
        # A.Print4()结果为：hello


class B:
    member = "this is a B."
b = B()

