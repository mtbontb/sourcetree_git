from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class Base:
    # 初始化方法
    def __init__(self):
        self.driver = webdriver.Firefox()
        # 最大化浏览器
        self.driver.maximize_window()
        # 打开url
        self.driver.get("http://localhost")

    # 查找元素方法 -->为以下三个方法服务 【难点】
    def base_find_element(self, loc, timeout=30, poll=0.5):# loc类型：列表或元组
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击元素方法
    def base_click(self, loc):
        # 调用查找元素方法
        self.base_find_element(loc).click()

    # 输入元素方法
    def base_input(self, loc, value):
        # 调用获取元素方法
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取元素信息方法
    def base_get_text(self, loc):
        # 看到 获取 先写return
        return self.base_find_element(loc).text
