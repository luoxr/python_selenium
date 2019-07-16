__author__ = "luo"

from TestSelenium.page.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    # 用户名输入框
    username_loc = (By.CSS_SELECTOR, ".loginPane input#phone")
    # 密码输入框
    password_loc = (By.CSS_SELECTOR, ".loginPane input#password")
    # 登录按钮
    login_loc = (By.CSS_SELECTOR, ".loginBtns > a")

    def open_login(self):
        """打开登录页面"""
        self.open()

    def input_username(self, username):
        """输入用户名"""
        self.send_keys(self.username_loc, text=username)

    def input_password(self, password):
        """输入密码"""
        self.send_keys(self.password_loc, text=password)

    def click_login_btn(self):
        """点击登录按钮"""
        self.click(self.login_loc)

    def find_login_pane(self):
        """查看是否有登录按钮，以此判断是否登录成功"""
        element = self.find_element(self.login_loc)
        return element

