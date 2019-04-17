#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""Client端-与我相关展示"""
        logger.info("不登录进入数据开放界面")
        Common.touch_by_id(self, ID.dataOpen)

        logger.info("查看是否可以进入数据开放界面")
        text_list = Common.get_text_by_class_name(self, ClassName.title, "span")
        self.assertTrue(Common.check_text_in_list(self, text_list, "数据总览："))

        logger.info("查看与我相关是否存在于界面中")
        text_list_2 = Common.get_text_by_class_name(self, ClassName.wrap_mine, "section")
        self.assertFalse(Common.check_text_in_list(self, text_list_2, "与我相关"))

        logger.info("登录")
        Common.touch_by_id(self, ID.loginBtn)
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("查看是否可以进入数据开放界面")
        Common.wait(self, 3)
        Common.touch_by_id(self, ID.dataOpen)
        text_list = Common.get_text_by_class_name(self, ClassName.title, "span")
        self.assertTrue(Common.check_text_in_list(self, text_list, "数据总览："))

        logger.info("查看与我相关是否存在于界面中")
        text_list_1 = Common.get_text_by_class_name(self, ClassName.wrap_mine, "section")
        self.assertTrue(Common.check_text_in_list(self, text_list_1, "与我相关"))


