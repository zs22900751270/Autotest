#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""云盘列表导航栏"""
        logger.info("打开客户端")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击进入内置应用界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用", "li")

        logger.info("点击进入云盘管理界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_submenu_title, "云盘管理", "div")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "云盘管理", "li")

        logger.info("查看是否进入云盘管理界面")
        text_list = Common.get_text_by_class_name(self, ClassName.menu_title)
        self.assertTrue(Common.check_text_in_list(self, text_list, "云盘管理"))

        logger.info("查看云盘列表导航栏")
        text_content_list = Common.get_text_by_class_name(self, ClassName.ivu_table_cell)
        self.assertTrue(Common.check_text_in_list(self, text_content_list, "用户名"))
        self.assertTrue(Common.check_text_in_list(self, text_content_list, "手机号"))
        self.assertTrue(Common.check_text_in_list(self, text_content_list, "云盘容量"))
        self.assertTrue(Common.check_text_in_list(self, text_content_list, "已使用"))
        self.assertTrue(Common.check_text_in_list(self, text_content_list, "状态"))
        self.assertTrue(Common.check_text_in_list(self, text_content_list, "操作"))


 
     
