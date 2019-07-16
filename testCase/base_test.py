__author__ = "luo"

import unittest
from time import sleep
from TestSelenium.page.factory_page import *

base_url = "http://10.10.10.101:5500/"


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n测试开始>>>>>>>>>>>>>>>>>>>")
        cls.driver = open_browser(browser="chrome")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(base_url)
        cls.driver.execute_script("localStorage.setItem('token', '%s');" % get_token())

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("测试结束<<<<<<<<<<<<<<<<<<<<\n")

