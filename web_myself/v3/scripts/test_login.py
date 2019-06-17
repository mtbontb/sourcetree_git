# 导包
import unittest

# 新建测试类 继承
from v3.page.page_login import PageLogin


class TestLogin(unittest.TestCase):
    login = None

    # 初始化
    def setUpClass(cls):
        # 实例化PageLogin
        cls.login = PageLogin()
        # 点击登录连接
        cls.login.page_click_login_link()

    # 结束
    def tearDownClass(cls):
        # 关闭driver
        cls.login.driver.quit()

    # 用户名不存在
    def test01_username_not_exists(self, username="13800001112", pwd="123456", verify_code="8888"):
        # 调用 登录业务方法
        self.login.page_login(username, pwd, verify_code)
        # 断言
        self.assertEqual("账号不存在!", self.login.page_get_error_info())
        # 点击 异常提示信息框
        self.login.page_click_error_btn()

    # 密码错误
    def test02_pwd_error(self, username="13800001111", pwd="1234567", verify_code="8888"):
        # 调用 登录业务方法
        self.login.page_login(username, pwd, verify_code)
        # 断言
        self.assertEqual("密码错误!", self.login.page_get_error_info())
        # 点击 异常提示信息框
        self.login.page_click_error_btn()
