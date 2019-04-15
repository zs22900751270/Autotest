#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""web登录都不输入"""
        logger.info("不输入账号密码点击登录")
        Common.touch_by_id(self, ID.handleSubmitBtn)
        logger.info("判断是否出现，提示请输入账号，密码")
        login_error_list_1 = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(BaseOperate.check_text_in_list(self, login_error_list_1, "账号不能为空"))
        self.assertTrue(BaseOperate.check_text_in_list(self, login_error_list_1, "密码不能为空"))

        logger.info("输入账号不输入密码，点击登录")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号", Content.register_count)
        Common.touch_by_id(self, ID.handleSubmitBtn)
        logger.info("判断是否出现提示请输入账号")
        login_error_list_2 = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertFalse(BaseOperate.check_text_in_list(self, login_error_list_2, "账号不能为空"))
        self.assertTrue(BaseOperate.check_text_in_list(self, login_error_list_2, "密码不能为空"))

        logger.info("不输入账号输入密码，点击登录")
        Common.refresh(self, 5)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", Content.login_password)
        Common.touch_by_id(self, ID.handleSubmitBtn)
        logger.info("判断是否出现提示请输入密码")
        login_error_list_3 = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(BaseOperate.check_text_in_list(self, login_error_list_3, "账号不能为空"))
        self.assertFalse(BaseOperate.check_text_in_list(self, login_error_list_3, "密码不能为空"))

        logger.info("输入账号输入密码，点击登录")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号", Content.register_count)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", Content.login_password)
        Common.touch_by_id(self, ID.handleSubmitBtn)

        logger.info("判断是否登录成功")
        self.assertTrue(Common.check_if_class_name_exist(self, ClassName.user_info))



     
