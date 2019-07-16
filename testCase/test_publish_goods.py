__author__ = "luo"

from ddt import ddt, data
from TestSelenium.testCase.base_test import BaseTest
from TestSelenium.page.factory_page import get_page
from TestSelenium.common.data_csv import get_data_all


@ddt
class PublishGoodsTest(BaseTest):
    """测试发布找货"""

    @data(*get_data_all("goods"))
    def test_publish(self, goods_data):
        """
        :return:
        """
        page = get_page(page_name="find-publish", driver=self.driver)

        page.open_publish_goods()
        # 输入内容（内容和图片至少填一项，添加图片功能和此逻辑待做）
        page.input_title_content(goods_data["title_content"])
        # 添加位置
        if goods_data["is_location"]:
            page.add_location()
        # 可见（所有人可见/仅商户可见）
        is_public = goods_data["is_public"]
        if page.get_visible_value() == "仅商户可见" and is_public == "所有人可见":
            page.click_visible()
            value = page.get_visible_value()
            self.assertEqual(is_public, value, msg="可见按钮失效")
        # 选择标签
        page.click_tag(goods_data["tag_name"])
        self.assertEqual(page.get_tag_active(), goods_data["tag_name"], msg="标签选择功能错误")
        # 确认发布
        page.publish()
        self.assertEqual("发布成功", page.is_success(), msg="发布找货失败")


