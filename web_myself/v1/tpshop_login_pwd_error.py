"""线性模型"""
# 导包
from selenium import webdriver
# 获取浏览器驱动对象
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)
# 打开 url
driver.get("http://localhost")
# 点击登录连接
driver.find_element_by_partial_link_text("登录").click()
# 定位用户名
username = driver.find_element_by_css_selector("#username")
# 清空
username.clear()
# 输入
username.send_keys("13800001111")
# 定位密码
pwd = driver.find_element_by_css_selector("#password")
# 清空密码
pwd.clear()
# 输入密码
pwd.send_keys("1234567")
# 定位验证码
verify_code = driver.find_element_by_css_selector("#verify_code")
# 清空
verify_code.clear()
# 输入验证码
verify_code.send_keys("8888")
# 点击登录按钮
driver.find_element_by_css_selector(".J-login-submit").click()
# 获取异常提示信息
result = driver.find_element_by_css_selector(".layui-layer-content").text
# 点击异常提示框 确定按钮
driver.find_element_by_css_selector(".layui-layer-btn0").click()
# 断言
assert "密码错误!" == result
# 关闭driver
driver.quit()