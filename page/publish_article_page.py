__author__ = "luo"

from TestSelenium.page.base_page import BasePage
from selenium.webdriver.common.by import By


class PublishArticlePage(BasePage):

    # 封面input
    cover_input_loc = (By.CSS_SELECTOR, "#uploadpoast-box input[type='file']")
    # 封面图片
    cover_loc = (By.CSS_SELECTOR, "section.uploadpoastshow")
    # 标题
    title_loc = (By.CSS_SELECTOR, "input#articletitle")
    # 正文box
    content_loc = (By.CSS_SELECTOR, ".zxeditor-content-wrapper")
    # 空正文
    empty_content_loc = (By.CSS_SELECTOR, ".zxeditor-content-wrapper.is-empty")
    # 正文中的p
    content_p_loc = (By.CSS_SELECTOR, ".zxeditor-content-wrapper > p")
    # 正文中上传图片的input
    content_input_loc = (By.CSS_SELECTOR, "#editorContainer > input[type='file']")
    # 正文中链接，内容a的属性href以及text
    content_link_loc = (By.CSS_SELECTOR, ".zxeditor-content-wrapper p.child-node-is-a a")
    # 正文中的图片
    content_pic_loc = (By.CSS_SELECTOR, ".zxeditor-content-wrapper p.child-node-is-img img")
    # 正文插入图片按钮
    add_pic_loc = (By.CSS_SELECTOR, "dd[data-name='pic']")
    # 正文插入链接按钮
    add_link_loc = (By.CSS_SELECTOR, "dd[data-name='link']")
    # 链接弹出框
    link_box_loc = (By.CSS_SELECTOR, ".zxeditor-linkinput-wrapper")
    # 链接url
    link_link_loc = (By.CSS_SELECTOR, ".zxeditor-linkinput-wrapper .linkinput-group>input:first-child")
    # 链接名称（选填）
    link_name_loc = (By.CSS_SELECTOR, ".zxeditor-linkinput-wrapper .linkinput-group>input:last-child")
    # 取消按钮
    link_cancel_loc = (By.CSS_SELECTOR, ".linkinput-footer>button.cancel-hook")
    # 确认按钮
    link_submit_loc = (By.CSS_SELECTOR, ".linkinput-footer>button.submit-hook")
    # 所有标签
    tags_loc = (By.CSS_SELECTOR, "div.choose-recommond-list > span")
    # 当前选中标签
    active_tag_loc = (By.CSS_SELECTOR, "div.choose-recommond-list > span.active")
    # 确认发布按钮
    publish_loc = (By.CSS_SELECTOR, ".find-header > a:last-child")
    # 发布成功/失败提示（.weui-toast_cancel）
    publish_success_loc = (By.CSS_SELECTOR, ".weui-toast p.weui-toast_content")

    def open_publish_article(self):
        """ 打开发布好文页面
        :return:
        """
        self.open()

    def add_cover(self, cover):
        """上传封面
        :param cover: 封面图片地址
        :return:
        """
        self.send_keys(self.cover_input_loc, text=cover)

    def is_add_cover(self):
        """判断封面是否上传成功
        :return: True -- 上传失败， None -- 上传成功
        """
        return self.visibility_element(self.cover_loc)

    def input_title(self, text):
        """输入标题
        :return:
        """
        self.send_keys(self.title_loc, text=text)

    def is_input_title(self, text):
        """检查是否输入成功
        :return: True -- 成功
        """
        return self.value_present(self.title_loc, text=text)

    def add_content_pic(self, pic):
        """
        添加正文图片
        :param pic: 图片地址
        :return:
        """
        # self.click(self.content_loc)
        js = """
            document.querySelector("#editorContainer > input[type='file']").setAttribute("style", "display:block")
        """
        self.base_driver.execute_script(js)
        self.send_keys(self.content_input_loc, text=pic)

    def is_add_content_pic(self):
        """
        判断图片是否添加成功
        :return: 返回图片个数
        """
        element = self.find_element(self.content_pic_loc)
        if element:
            return True
        else:
            return False

    def click_add_content_link(self):
        """
        点击添加链接按钮
        :return:
        """
        self.click(self.add_link_loc)

    def is_add_box_flex(self):
        """
        判断是否点击成功。即link_box_loc可见
        :return: True -- 点击失效，False -- 点击成功
        """
        return self.visibility_element(self.link_box_loc)

    def add_content_link(self, url, url_name):
        """
        添加链接
        :param url: 链接
        :param url_name: 链接名称
        :return:
        """
        if url.startswith("http://") or url.startswith("https://"):
            self.send_keys(self.link_link_loc, url)
            if url_name.strip() != "" and url_name.strip():
                self.send_keys(self.link_name_loc, url_name)
            self.click(self.link_submit_loc)
        else:
            self.click(self.link_cancel_loc)

    def is_add_content_link(self, url):
        """
        判断链接是否添加成功，content_link_loc
        :return: True -- 成功
        """
        element = self.find_element(self.content_link_loc)
        if element:
            get_url = element.get_attribute("href")
            if get_url == url:
                return True
            return False
        else:
            return False

    def add_content_text(self, text):
        """
        添加正文内容
        :param text: 文字
        :return:
        """
        if text:
            if self.is_content_empty():
                # 正文空
                js = """
                    var content = document.querySelector('.zxeditor-content-wrapper > p');
                    content.innerText = '%s';
                    """ % text
            else:
                # 正文有内容
                js = """
                    var content = document.getElementsByClassName('zxeditor-content-wrapper')[0];
                    var p = document.createElement('p');
                    p.innerHTML = '<p>%s</p>';
                    content.appendChild(p);
                    """ % text
            self.click(self.content_loc)
            self.base_driver.execute_script(js)

    def is_add_content_text(self, text):
        """
        判断正文内容是否添加成功
        :return: True -- 添加成功，False -- 添加失败
        """
        text_loc = (By.XPATH, "/html/body/article/div/div/div/p[text()='%s']" % text)
        element = self.find_element(text_loc)
        if element:
            return True
        return False

    def is_content_empty(self):
        """
        判断正文是否为空
        :return: True -- 为空，False -- 不为空
        """
        element = self.find_element(self.empty_content_loc)
        if element:
            return True
        return False

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
        返回被点击的标签内容
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
        是否发布成功，五种提示：
        1、请添加封面
        2、请填写标题
        3、请选择标签
        4、请添加文章内容
        5、发布成功
        :return: 成功
        """
        element = self.find_element(self.publish_success_loc)
        if element:
            return element.text.strip()
        return False




