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
        Common.delete_department_by_name(self, "zs_test")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.quit(self)

    def test_step(self):
        u"""pc-个人用户禁用/启用单个账号"""
        logger.info("登录后端")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户管理", "span", 2)

        logger.info("对单独一个账号进行启用或禁用")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "输入账号或姓名进行搜索",
                                                       Content.spare_count+"\n")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_ghost_small, "禁用", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入原因", "reason")
        Common.touch_by_id(self, ID.attendModelOkBtn)
        con = Common.get_text_by_class_name(self, ClassName.ivu_table_row, "tr")[0]
        self.assertTrue("禁用" in con)
        self.assertEqual(con.count("禁用"), 2)

        logger.info("点击启用")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_ghost_small, "启用", "button")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入原因", "reason")
        Common.touch_by_id(self, ID.attendModelOkBtn)
        con = Common.get_text_by_class_name(self, ClassName.ivu_table_row, "tr")[0]
        self.assertTrue("启用" in con)
        self.assertEqual(con.count("启用"), 2)

