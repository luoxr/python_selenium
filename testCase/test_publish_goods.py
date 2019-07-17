__author__ = "luo"

from time import sleep
from ddt import ddt, data
from TestSelenium.testCase.base_test import BaseTest
from TestSelenium.page.factory_page import get_page
from TestSelenium.common.data_csv import get_data_all
from TestSelenium.common.data_image import get_image_path


@ddt
class PublishGoodsTest(BaseTest):
    """测试发布找货"""

    @data(*get_data_all("goods"))
    def test_publish(self, goods_data):
        """
        :return:
        """
        page = get_page(page_name="find-publish", driver=self.driver)

        # 打开页面
        page.open_publish_goods()

        title_content = goods_data["title_content"]
        pic_path = goods_data["pic_path"]

        # 输入找货描述
        if title_content.strip() != "":
            page.input_title_content(title_content)
        # 上传图片
        pic_elements = None
        if pic_path.strip() != "":
            pics = pic_path.strip().split(",")
            # 循环上传图片
            i = 1
            for pic in pics:
                # 上传图片
                pic_path = get_image_path(pic)
                if not pic_path:
                    continue
                page.upload_pic(pic_path)
                # 判断是否上传成功
                sleep(0.5)
                pic_elements = page.upload_success_pic()
                if len(pic_elements) == i:
                    if len(pic_elements) == 3:
                        self.assertTrue(page.pic_box_display(), msg="已上传3张图片，图片上传按钮未隐藏！")
                        break
                    i += 1
                else:
                    self.assertEqual(len(pic_elements), i, msg="上传失败第%s张图片时失败！" % i)
            # self.assertIsNotNone(pic_elements, msg="上传图片失败！")
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
        if goods_data["tag_name"].strip() != "":
            page.click_tag(goods_data["tag_name"])
            self.assertEqual(page.get_tag_active(), goods_data["tag_name"], msg="没有此标签/点击标签功能出错")
        # 确认发布
        page.publish()

        # 找货描述、图片无时，提示：找货描述，图片至少填一项
        # 找货描述、图片有其一，标签无时，提示：请选择一个标签
        # 找货描述、图片有其一，标签也有时，提示：发布成功

        if title_content.strip() == "" and pic_elements is None:
            self.assertEqual("找货描述，图片至少填一项", page.is_success(), msg="找货描述，图片至少填一项 功能错误")

        elif (title_content.strip() != "" or pic_elements) \
                and goods_data["tag_name"].strip() == "":
            self.assertEqual("请选择一个标签", page.is_success(), msg="请选择一个标签 功能错误")
        else:
            self.assertEqual("发布成功", page.is_success(), msg="发布找货失败")
        # if title_content.strip() == "" and (pic_path.strip() == "" or pic_elements is None):
        #     self.assertEqual("找货描述，图片至少填一项", page.is_success(), msg="找货描述，图片至少填一项功能错误")
        # # 标签
        # if goods_data["tag_name"].strip() == "" and tag_active is False:
        #     self.assertEqual("请选择一个标签", page.is_success(), msg="请选择一个标签功能错误")
        #
        # self.assertEqual("发布成功", page.is_success(), msg="发布找货失败")
