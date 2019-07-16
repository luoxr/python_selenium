__author__ = "luo"

import ddt
from TestSelenium.testCase.base_test import BaseTest
from TestSelenium.page.factory_page import get_page
from TestSelenium.common.data_csv import get_data_all


@ddt.ddt
class LoginTest(BaseTest):
    """测试首页"""

    @ddt.data(*get_data_all("login"))
    def test_login(self, login_data):
        """测试登录，判断是否登录成功
        :return:
        """
        page = get_page(page_name="login", driver=self.driver)

        page.open_login()
        page.input_username(login_data["phone"])
        page.input_password(login_data["password"])
        page.click_login_btn()
        element = page.find_login_pane()
        self.assertEqual(None, element, msg="登录失败！")



