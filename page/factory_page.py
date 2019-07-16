__author__ = "luo"

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from TestSelenium.page.login_page import LoginPage
from TestSelenium.page.publish_goods_page import PublishGoodsPage

base_url = "http://10.10.10.101:5500/"


def get_page(page_name, driver):
    """公共方法，返回页面对象
    :param page_name: 页面名
    :param driver:
    :return: 页面对象
    """
    url = base_url + page_name + ".html"
    page = {
        "login": LoginPage(base_driver=driver, base_url=url),
        "find-publish": PublishGoodsPage(base_driver=driver, base_url=url)
    }

    return page.get(page_name)


def open_browser(browser='chrome'):
    """打开浏览器
    :param browser:
    :return:
    """
    try:
        if browser == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif browser == "chrome":
            # driver = webdriver.Chrome()
            chrome_options = Options()
            chrome_options.add_argument('disable-infobars')  # 去除提示：正受到自动测试软件的控制
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            # chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
            # chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            # chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 手动指定使用的浏览器位置
            driver = webdriver.Chrome(chrome_options=chrome_options)
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        else:
            print("没有找到浏览器")
    except Exception as msg:
        print("%s" % msg)


def get_token():
    """获得用户token
    :return:
    """
    url = "http://10.10.10.101:8083/rest/mobile/common/vip/login"
    data = {
        "phone": "18012340004",
        "password": "dec5d7b46b13d0c39c3f185de36b25bf",
        "plat": 3
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    response = requests.post(url=url, data=data, headers=headers)
    is_success = response.json()["success"]
    token = None
    if is_success:
        token = response.json()["data"]["restToken"]
    return token


if __name__ == "__main__":

    print(get_token())

