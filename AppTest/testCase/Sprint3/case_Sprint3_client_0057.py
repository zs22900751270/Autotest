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
        u"""忘记密码界面不输入任何字符"""
        Common.touch_text_by_class_name(self, ClassName.ivu_col_span_5, "忘记密码", "div")
        Common.wait(self, 10)
        handles = Common.get_window_handle(self)
        Common.switch_window_handle(self, handles[1])

        logger.info("点击获取验证码,判断是否出现错误提示")
        Common.touch_by_id(self, ID.checkUpdatePwdcodeBtn)

        logger.info("判断是否进入修改密码界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, text_list, "手机号不能为空"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "验证码不能为空"))



     
