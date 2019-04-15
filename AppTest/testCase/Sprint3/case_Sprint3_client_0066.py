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

    def check_error_tip(self):
        global check_res
        check_res = False
        i = 0
        while i < 5:
            error_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
            if Common.check_text_in_list(self, error_list, "验证码已失效,请重新获取"):
                check_res = True
                break
            i += 1
            Common.wait(self, 1)

    def test_step(self):
        u"""输入超时的验证码"""
        logger.info("获取验证码")
        Common.touch_text_by_class_name(self, ClassName.ivu_col_span_5, "忘记密码", "div")
        Common.wait(self, 10)
        handles = Common.get_window_handle(self)
        Common.switch_window_handle(self, handles[1])

        logger.info("输入超过11位数字的号码")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号",
                                                       Content.register_count)

        logger.info("点击获取验证码")
        Common.touch_by_id(self, ID.checkUpdatePwdcodeBtn)

        logger.info("获取验证码")
        ident_code = Common.get_identifying_code(self, Content.register_count)

        for i in range(1, 11):
            logger.info("------%s------" % i)
            Common.wait(self, 60)
            Common.touch_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码")

        logger.info("输入已超时的验证码")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码", ident_code)
        threading.Thread(target=self.check_error_tip, args=()).start()
        Common.touch_by_id(self, ID.checkUpdatePwdcodeBtn)
        self.assertTrue(check_res)


