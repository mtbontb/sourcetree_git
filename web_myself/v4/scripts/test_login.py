"""
    目标：po登录业务实现
    结构：
        新建测试类

            # 初始化

            # 结束

            # 测试方法
"""
import unittest
from parameterized import parameterized
from v4.page.page_login import PageLogin


# 定义获取测试数据函数
def get_data():
    return [("13800001112","123456","8888", "账号不存在!"),("13123456789","1234567","8888", "密码错误!")]


class TestLogin(unittest.TestCase):
    login = None
    # 初始化方法
    @classmethod
    def setUpClass(cls):
        # 获取PageLogin 对象
        cls.login = PageLogin()
        # 点击登录连接
        cls.login.page_click_login_btn_link()

    # 结束方法
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.login.driver.quit()

    # 测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, verify_code, expect):
        # 调用登录业务方法
        self.login.page_login(username, pwd, verify_code)
        # 断言
        self.assertEqual(expect,self.login.page_get_error_info())
        # 点击异常提示框
        self.login.page_click_error_btn()

