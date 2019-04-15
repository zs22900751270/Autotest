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
        u"""web无手机号码获取验证码"""
        logger.info("进入注册界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_col_offset_19, "注册账号", "div")

        logger.info("在不输入手机号的情况下，点击获取验证码")
        Common.touch_by_id(self, ID.getRegisterCodeBtn)

        error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(Common.check_text_in_list(self, error_list, "请输入手机号"))



     
