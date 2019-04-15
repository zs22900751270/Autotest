#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        logger.info("收尾工作")
        Common.quit(self)

    def test_step(self):
        u"""导航栏点击服务"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "服务")
        Common.wait(self, 2)

        logger.info("点击数据可视化")
        Common.touch_text_by_class_name(self, ClassName.center, "数据可视化")
        Common.wait(self, 2)

        logger.info("判断是否进入数据可视化界面")
        result = Common.check_if_class_name_exist(self, ClassName.no_html_text, "div")
        self.assertTrue(result)

        logger.info("判断界面布局")
        re1 = Common.check_if_class_name_exist(self, ClassName.left)
        re2 = Common.check_if_class_name_exist(self, ClassName.right)
        self.assertTrue(re1)
        self.assertTrue(re2)


 
    
