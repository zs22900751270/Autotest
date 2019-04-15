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
        Common.modify_user_locked_status_by_phone(self, Content.spare_count)
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""管理端-用户列表支持设置每页显示条数验证"""
        logger.info("登录后端")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户管理", "span", 2)

        logger.info("查看列数是否相同")
        col_num = Common.get_results_by_class_name_blank(self, "tr", ClassName.ivu_table_row)
        self.assertEqual(len(col_num), 10)

