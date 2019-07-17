__author__ = "luo"

from TestSelenium.page.base_page import BasePage
from selenium.webdriver.common.by import By


class PublishGoodsPage(BasePage):

        # 寻物内容
        title_content_loc = (By.ID, "titlecontent")
        # 上传图片按钮
        upload_pic_loc = (By.CSS_SELECTOR, "#find-upload-pic input[type='file']")
        # 图片
        pic_loc = (By.CSS_SELECTOR, "#find-upload-pic > span")
        # 图片右上角的关闭按钮
        del_pic_loc = (By.CSS_SELECTOR, "#find-upload-pic > span > a.delpng")
        # 图片box，上传3张后，display:none
        pic_box_loc = (By.ID, "find-upload-btn-box")
        # 定位按钮
        location_loc = (By.ID, "locationCity")
        # 可见权限按钮
        visible_loc = (By.CSS_SELECTOR, ".find-isopen input[type='checkbox']")
        # 可见权限的值
        visible_value_loc = (By.CSS_SELECTOR, ".find-isopen div.weui-cell__bd")
        # 所有标签
        tags_loc = (By.CSS_SELECTOR, "div.choose-recommond-list > span")
        # 当前选中标签
        active_tag_loc = (By.CSS_SELECTOR, "div.choose-recommond-list > span.active")
        # 确认发布按钮
        publish_loc = (By.CLASS_NAME, "find-publish-btn")
        # 发布成功/失败提示（.weui-toast_cancel）
        publish_success_loc = (By.CSS_SELECTOR, ".weui-toast p.weui-toast_content")

        def open_publish_goods(self):
            """打开发布页面
            :return:
            """
            self.open()
            # self.base_driver.execute_script("localStorage.setItem('token', '%s');" % get_token())

        def input_title_content(self, text):
            """
            输入找货内容
            :param text:
            :return:
            """
            self.send_keys(self.title_content_loc, text=text)

        def title_content_value(self):
            """
            查询找货内容
            :return:
            """
            return self.find_element(self.title_content_loc).get_attribute("value")

        def upload_pic(self, pic):
            """上传图片
            :param pic: 图片路径
            :return:
            """
            self.send_keys(self.upload_pic_loc, text=pic)

        def upload_success_pic(self):
            """
            查找图片，判断图片是否上传成功
            :return: 返回elements
            """
            elements = self.find_elements(self.pic_loc)
            return elements

        def pic_box_display(self):
            """
            查找box，判断上传按钮是否在
            :return: False -- 不存在，已3张，True -- 存在，不足3张
            """
            return self.visibility_element(self.pic_box_loc)

        def add_location(self):
            """添加位置
            :return:
            """
            self.click(self.location_loc)

        def click_visible(self):
            """
            点击可见权限
            :return:
            """
            self.click(self.visible_loc)

        def get_visible_value(self):
            """
            获取可见权限的值，True -- 所有人可见  False -- 仅商户可见
            :return:
            """
            value = None
            value_element = self.find_element(self.visible_value_loc)
            if value_element:
                value = value_element.text
            return value

        def click_tag(self, tag):
            """
            点击一个标签
            :param tag: 标签名
            :return:
            """
            tag_loc = (By.XPATH, "/html/body/section/div/span[text()='%s']" % tag)
            self.click(tag_loc)

        def get_tag_active(self):
            """
            被点击的标签内容
            :return:
            """
            element = self.find_element(self.active_tag_loc)
            if element:
                return element.text
            return None

        def publish(self):
            """
            确认发布
            :return:
            """
            self.click(self.publish_loc)

        def is_success(self):
            """
            是否发布成功，三种提示：
            1、找货描述，图片至少填一项
            2、请选择一个标签
            3、发布成功
            :return: None 成功
            """
            element = self.find_element(self.publish_success_loc)
            if element:
                return element.text.strip()
            return False

