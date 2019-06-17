from selenium.webdriver.common.by import By

"""以下为登录页面配置信息"""
# 登录连接
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 输入用户名
login_username = By.CSS_SELECTOR, "#username"
# 输入密码
login_pwd = By.CSS_SELECTOR, "#password"
# 输入验证码
login_verify_code = By.CSS_SELECTOR, "#verify_code"
# 点击登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 获取异常提示信息
login_error_info = By.CSS_SELECTOR, ".layui-layer-content"
# 点击异常提示框 确认
login_error_btn_ok = By.CSS_SELECTOR, ".layui-layer-btn0"