from selenium import webdriver

"""
    说明：将每步操作单独封装一个函数，如果需要一个封装调用所有操作，组合一个业务方法
"""
class PageLogin:
    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = webdriver.Firefox()
        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(30)
        # 打开 url
        self.driver.get("http://localhost")

    # 点击登录连接
    def page_click_login_link(self):
        self.driver.find_element_by_partial_link_text("登录").click()

    # 输入用户名
    def page_input_username(self, username):
        el = self.driver.find_element_by_css_selector("#username")
        el.clear()
        el.send_keys(username)

    # 输入密码
    def page_input_pwd(self, password):
        el = self.driver.find_element_by_css_selector("#password")
        el.clear()
        el.send_keys(password)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        el = self.driver.find_element_by_css_selector("#verify_code")
        el.clear()
        el.send_keys(verify_code)

    # 点击确定按钮
    def page_click_confirm_btn(self):
        self.driver.find_element_by_css_selector(".J-login-submit").click()

    # 获取异常提示信息
    def page_get_error_info(self):
        return self.driver.find_element_by_css_selector(".layui-layer-content").text

    # 点击异常提示框 确定按钮
    def page_click_error_btn(self):
        self.driver.find_element_by_css_selector(".layui-layer-btn0").click()

    # 组合 登录业务方法 --->在业务层调用
    def page_login(self, username, pwd, verify_code):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(verify_code)
        self.page_click_confirm_btn()