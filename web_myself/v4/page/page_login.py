"""点击
    类名：使用大驼峰形式将模块名称抄进来，有下划线，去掉下划线；
    方法：涉及到的元素，每个元素的操作单独封装1个方法；组合业务方法
"""
from v4 import page
from v4.base.base import Base


class PageLogin(Base):
    # 点击登录 链接
    def page_click_login_btn_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        self.base_input(page.login_verify_code, verify_code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取异常提示信息文本
    def page_get_error_info(self):
        return self.base_get_text(page.login_error_info)

    # 点击异常提示框 确定按钮
    def page_click_error_btn(self):
        self.base_click(page.login_error_btn_ok)

    # 组合业务方法 -->在业务层调用
    def page_login(self, username, pwd, verify_code):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(verify_code)
        self.page_click_login_btn()
