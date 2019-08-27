__author__ = "luo"

from time import sleep
from ddt import ddt, data
from TestSelenium.testCase.base_test import BaseTest
from TestSelenium.page.factory_page import get_page
from TestSelenium.common.data_csv import get_data_all
from TestSelenium.common.data_image import get_image_path


@ddt
class PublishArticleTest(BaseTest):
    """测试发布好文"""

    @data(*get_data_all("article"))
    def test_publish(self, article_data):
        """
        :return:
        """
        page = get_page(page_name="find-publisharticle", driver=self.driver)

        # 打开页面
        page.open_publish_article()

        # 上传封面
        pic = article_data["cover"].strip()
        cover = get_image_path(pic)
        if cover:
            page.add_cover(cover)
            sleep(0.5)
            self.assertIsNone(page.is_add_cover(), msg="上传封面失败")

        # 添加标题
        title = article_data["title"].strip()
        if title:
            page.input_title(title)
            self.assertTrue(page.is_input_title(title), msg="输入标题失败")

        # 输入文字
        text = article_data["text"].strip()
        if text:
            page.add_content_text(text)
            self.assertTrue(page.is_add_content_text(text), msg="输入正文文字失败")

        # 添加链接
        link = article_data["link"].strip()
        link_name = article_data["link_name"].strip()
        page.click_add_content_link()
        if page.is_add_box_flex():
            self.assertTrue(False, msg="添加链接按钮失效")
        else:
            page.add_content_link(link, link_name)
            self.assertTrue(page.is_add_content_link(link), msg="添加链接失败")

        # 添加图片
        pic = article_data["pic"].strip()
        if pic:
            path = get_image_path(pic)
            if path:
                page.add_content_pic(path)
                self.assertTrue(page.is_add_content_pic(), msg="添加图片失败")
        # 点击标签
        if article_data["tag"].strip() != "":
            page.click_tag(article_data["tag"])
            self.assertEqual(page.get_tag_active(), article_data["tag_name"], msg="没有此标签/点击标签功能出错")
        # 发布
        page.publish()

        # 没有封面提示：请添加封面
        # 没有标题：请填写标题
        # 没有标签：请选择标签
        # 正文中，文字、链接、图片都没有：请添加文章内容
        # 发布成功
        pass

