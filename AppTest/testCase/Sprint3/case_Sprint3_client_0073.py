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
        u"""修改密码，错误的确认密码和错误的密码"""
        Common.touch_text_by_class_name(self, ClassName.ivu_col_span_5, "忘记密码", "div")
        Common.wait(self, 10)
        handles = Common.get_window_handle(self)
        Common.switch_window_handle(self, handles[1])
        logger.info("输入手机号")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号",
                                                       "19802990115")

        logger.info("点击获取验证码,判断是否出现错误提示")
        Common.touch_by_id(self, ID.getUpdatePwdCodeBtn)
        identify_code = Common.get_identifying_code(self, Content.register_count)
        logger.info("输入错误的验证码，点击确定，查看错误提示")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码",
                                                       identify_code)
        Common.touch_by_id(self, ID.checkUpdatePwdcodeBtn)

        logger.info("密码框与确认密码框输入不同字符")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", "qwe123")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "确认密码", "123qwe")
        Common.touch_by_xpath(self, WebControl.web_fgpd_ok_button)
        Common.touch_by_id(self, ID.updatePasswordBtn)
        error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(Common.check_text_in_list(self, error_list, "两次输入密码不一致!"))

        logger.info("密码框与确认密码框输入不同字符")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", "zhangsen123")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "确认密码", "123zhangsen")
        Common.touch_by_xpath(self, WebControl.web_fgpd_ok_button)
        Common.touch_by_id(self, ID.updatePasswordBtn)
        error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(Common.check_text_in_list(self, error_list, "两次输入密码不一致!"))



     
