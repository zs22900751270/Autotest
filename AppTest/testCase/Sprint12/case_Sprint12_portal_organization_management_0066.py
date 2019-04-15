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
        Common.modify_user_locked_status_by_phone(self, Content.register_count)
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.quit(self)

    def test_step(self):
        u"""pc-个人用户搜索长度限制"""
        logger.info("登录后端")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户管理", "span", 2)

        logger.info("对单独一个账号进行启用或禁用")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "输入账号或姓名进行搜索",
                                                       Content.spare_count[1:]+"\n")
        logger.info("是否搜索成功")
        tr_ele = Common.get_results_by_class_name_blank(self, "tr", ClassName.ivu_table_row)
        self.assertEqual(len(tr_ele), 1)

        logger.info("查看搜索框是否有长度限制")
        sear = Common.get_element_by_placeholder_and_class_name(self, ClassName.ivu_input, "输入账号或姓名进行搜索")
        self.assertEqual(sear.get_attribute("maxlength"), "11")

