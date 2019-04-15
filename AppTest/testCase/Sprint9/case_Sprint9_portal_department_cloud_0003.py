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
        u"""后台管理-部门云盘-权限测试"""
        logger.info("打开客户端")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击进入内置应用界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "内置应用")

        logger.info("进入邮箱管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "邮箱管理", "span", times=1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "邮箱管理", "span", times=2)

        logger.info("查看是否进入邮箱管理界面")
        header_ele = Common.get_result_by_class_name(self, ClassName.ivu_table_header)
        th_list = Common.get_tag_name_by_element(self, header_ele, "th", None)
        th_text = Common.get_text_by_elements(self, th_list)
        self.assertTrue(Common.check_text_in_list(self, th_text, "用户名"))
        self.assertTrue(Common.check_text_in_list(self, th_text, "手机号"))
        self.assertTrue(Common.check_text_in_list(self, th_text, "邮箱地址"))
        self.assertTrue(Common.check_text_in_list(self, th_text, "容量"))
        self.assertTrue(Common.check_text_in_list(self, th_text, "状态"))
        self.assertTrue(Common.check_text_in_list(self, th_text, "操作"))

