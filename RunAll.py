__author__ = "luo"

import os
import sys
import unittest
from BeautifulReport import BeautifulReport
from TestSelenium.testCase.test_login import LoginTest
from TestSelenium.testCase.test_publish_goods import PublishGoodsTest


path = os.getcwd() + "/RunAll.py"
sys.path.append(path)
# test_cases = (LoginTest,PublishGoodsTest)
test_cases = (PublishGoodsTest,)


def whole_suite():

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


if __name__ == '__main__':

    report_name = "测试报告"
    runner = BeautifulReport(whole_suite())
    runner.report(filename=report_name, description='python+selenium+unittest测试')

