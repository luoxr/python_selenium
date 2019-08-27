__author__ = "luo"

import requests
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class BasePage(object):
    """page Object设计模式，所有页面的基类，定义公共方法、变量"""
    def __init__(self, base_driver, base_url, timeout=5):
        self.base_driver = base_driver
        self.base_url = base_url
        self.timeout = timeout

    def open(self):
        """打开网页
        注释代码：在页面严格规定了title的情况下打开，判断页面是否被打开
        :return:
        """
        self.base_driver.get(url=self.base_url)
        # try:
        #     WebDriverWait(driver=self.base_driver, timeout=self.timeout).until(EC.title_contains(self.page_title))
        # except TimeoutException:
        #     assert u"页面 %s请求超时：%s" % self.base_url
        # except Exception as msg:
        #     assert u"页面 %s打开失败：%s" % (self.base_url, msg)

    def find_element(self, locator):
        """定位一个元素
        is_displayed: 存在于dom树中
        :param locator: 元祖类型
        :return:
        """
        try:
            WebDriverWait(driver=self.base_driver, timeout=self.timeout)\
                .until(lambda x: x.find_element(*locator).is_displayed)
            element = self.base_driver.find_element(*locator)
            return element
        except TimeoutException:
            print(u"请求超时，未能找到元素 %s" % (locator,))
        except NoSuchElementException:
            print(u"当前页面中未能找到元素 %s" % (locator,))
        except Exception as msg:
            print(u"当前页面未能找到元素 %s，%s" % (locator, msg))

    def visibility_element(self, locator):
        """
        判断某元素是否不存在于dom中或不可见
        :param locator:
        :return: 不可见返回True，可见为None
        """
        try:
            WebDriverWait(driver=self.base_driver, timeout=self.timeout)\
                .until(EC.invisibility_of_element_located(locator))
            return True
        except Exception as msg:
            print(u"元素可见，%s" % msg)

    def value_present(self, locator, text):
        """
        判断文本是否存在于元素的value值中
        :param locator: 元素
        :param text: 文本
        :return: 存在返回True
        """
        try:
            WebDriverWait(driver=self.base_driver, timeout=self.timeout)\
                .until(EC.text_to_be_present_in_element_value(locator, text))
            return True
        except Exception as msg:
            print(u"元素%s 不存在该value值，%s" % (locator, msg))

    def find_elements(self, locator):
        """定位一组元素
        :param locator:
        :return:
        """
        try:
            WebDriverWait(self.base_driver, timeout=self.timeout)\
                .until(EC.presence_of_all_elements_located(locator))
            elements = self.base_driver.find_elements(*locator)
            return elements
        except TimeoutException:
            print(u"请求超时，未能找到元素 %s" % (locator,))
        except NoSuchElementException:
            print(u"当前页面中未能找到元素 %s" % (locator,))
        except Exception as msg:
            print(u"当前页面未能找到元素 %s，%s" % (locator, msg))

    def click(self, locator):
        """点击元素
        :param locator:
        :return:
        """
        element = self.find_element(locator)
        if element:
            element.click()
        else:
            print("没有找到该点击元素")
        sleep(1)

    def send_keys(self, locator, text):
        """向元素输入内容
        :param locator:
        :param text
        :return:
        """
        if not text:
            print("输入内容为空")
            return
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print("没有找到可输入元素")

    def refresh_(self):
        self.base_driver.refresh()
