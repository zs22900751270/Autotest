#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *
file_path = "\\resource\\File\\html\\test_htm.html"
template_name = "template"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        logger.info("收尾工作")
        Common.quit(self)

    def test_step(self):
        u"""选择模板文件"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理,点击数据集管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        if Common.get_display_status_by_text(self, "大数据展示"):
            Common.touch_text_by_class_name(self, ClassName.layout_text, "大数据展示")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "模版上传")
        Common.wait(self, 3)

        logger.info("输入名称")
        get_text = Common.get_text_by_class_name(self, ClassName.menu_title)[0]
        logger.info(get_text)
        self.assertTrue(get_text == "模版上传")



    
