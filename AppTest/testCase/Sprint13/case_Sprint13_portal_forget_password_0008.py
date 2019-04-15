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
        u"""PC—忘记密码界面输入用过的验证码"""
        logger.info("点击修改密码")
        fgt_psd = Common.get_element_by_class_name_and_text(self, "a", "", "忘记密码")
        Common.touch_by_element(self, fgt_psd)

        logger.info("查看是否进入修改密码界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.checkUpdatePwdcodeBtn))

        logger.info("输入手机号获取验证码")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号", Content.register_count)
        Common.touch_by_id(self, ID.getUpdatePwdCodeBtn)
        ident_code = Common.get_identifying_code(self, Content.register_count)
        for i in range(2):
            Common.wait(self, 30)
            Common.touch_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码")
        Common.touch_by_id(self, ID.getUpdatePwdCodeBtn)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码", ident_code)
        Common.touch_by_id(self, ID.checkUpdatePwdcodeBtn)

        logger.info("查看是否有错误提示")
        err_tip = Common.get_text_by_class_name(self, ClassName.sweet_alert_showsweetalert_visible, "div")
        self.assertTrue(Common.check_text_in_list(self, err_tip, "验证码输入错误"))




