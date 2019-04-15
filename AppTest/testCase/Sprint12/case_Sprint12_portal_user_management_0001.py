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
        u"""管理端-添加用户页面显示"""
        logger.info("登录后端")
        Common.rename_user_realname_by_phone(self, Content.spare_count, Content.spare_count_realname)
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("进入用户管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "用户管理", "li")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户管理", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "用户管理", "span", 2)

        logger.info("点击添加用户")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_ghost, "添加用户", "button")

        logger.info("查看参数显示是否完整")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_label, "label")
        self.assertTrue(Common.check_text_in_list(self, text_list, "账号"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "真实姓名"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "用户类型"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "角色"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "性别"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "生日"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "邮箱"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "居住地"))


