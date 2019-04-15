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
        u"""输入错误的验证码"""
        logger.info("进入忘记密码界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_col_span_5, "忘记密码", "div")
        handles = Common.get_window_handle(self)
        Common.switch_window_handle(self, handles[1])

        logger.info("输入超过11位数字的号码")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号",
                                                       Content.register_count)

        logger.info("点击获取验证码按钮")
        Common.touch_by_id(self, ID.getUpdatePwdCodeBtn)

        logger.info("在验证码框输入验证码加其他数字")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码", "@#￥%")
        Common.touch_by_id(self, ID.checkUpdatePwdcodeBtn)
        get_ident = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, get_ident, "请输入6位数字验证码"))


