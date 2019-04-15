#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *


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

        logger.info("点击上传文件")
        Common.upload_file(self, ClassName.ivu_upload_input, "html", "test_htm.html")

        logger.info("判断是否上传文件成功")
        get_iframe = Common.get_results_by_class_name_blank(self, "iframe", ClassName.html_render)
        BaseOperate.wait(self, 1)
        Common.switch_to_frame(self, get_iframe[0])
        new_iframe_content = Common.get_text_by_xpath(self, "/html/body")
        self.assertTrue(new_iframe_content == "this html file only use to test")



    
