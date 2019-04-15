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

        logger.info("不输入点击保存")
        Common.touch_by_id(self, ID.attendModelOkBtn, times=2)
        err_tip = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, err_tip, "请填写手机号码"))
        self.assertTrue(Common.check_text_in_list(self, err_tip, "请填写真实姓名"))
        self.assertTrue(Common.check_text_in_list(self, err_tip, "请选择性别"))
        self.assertTrue(Common.check_text_in_list(self, err_tip, "请选择生日"))
        self.assertTrue(Common.check_text_in_list(self, err_tip, "请填写邮箱地址"))

