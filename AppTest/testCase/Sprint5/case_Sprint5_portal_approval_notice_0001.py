#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
theme_name = "theme_add_01"
theme_name_new = "theme_add_new"


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
        u"""通知管理页面点击发公告会跳转到发公告界面"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击运维管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "运维管理")
        Common.wait(self, 2)

        logger.info("判断是否进入公告发布界面")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "标准数据字典管理")
        text_exist = Common.get_results_by_class_name_blank(self, ClassName.ivu_btn_primary, "button")
        self.assertIsNotNone(text_exist)



    
