#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *
longtext = "zs123456789123456798123456789123456789123465789"


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
        u"""修改密码失败"""
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

        logger.info("输入纯数字")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", "123456")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "确认密码", "123456")
        Common.touch_by_id(self, ID.updatePasswordBtn)
        error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(Common.check_text_in_list(self, error_list, "密码只包括6-32位的字符和数字"))

        logger.info("输入纯字母")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", "zhangsen")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "确认密码", "zhangsen")
        Common.touch_by_id(self, ID.updatePasswordBtn)
        error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(Common.check_text_in_list(self, error_list, "密码只包括6-32位的字符和数字"))

        logger.info("输入不足六位字符")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", "zs123")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "确认密码", "zs123")
        Common.touch_by_id(self, ID.updatePasswordBtn)
        error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(Common.check_text_in_list(self, error_list, "密码只包括6-32位的字符和数字"))

        logger.info("输入超过32位字符")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入密码", longtext)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "确认密码", longtext)
        Common.touch_by_id(self, ID.updatePasswordBtn)
        error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(Common.check_text_in_list(self, error_list, "密码只包括6-32位的字符和数字"))



     
