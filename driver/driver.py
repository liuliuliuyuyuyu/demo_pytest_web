from selenium import webdriver


class Driver:
    __driver=None
    __options=None
    is_open = True

    # 获取浏览器驱动

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__options = webdriver.ChromeOptions()
            cls.__options.add_argument('--start-maximized')
            cls.__options.add_argument('--headless')
            cls.__options.add_argument('--disable-gpu')
            cls.__driver = webdriver.Chrome(chrome_options=cls.__options)
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            # 设置超时
            cls.__driver.implicitly_wait(20)
        return cls.__driver

    # 关闭浏览器驱动
    @classmethod
    def quit_dirver(cls):
        if cls.is_open and cls.__driver is not None:
            cls.get_driver().quit()
            cls.__driver = None
