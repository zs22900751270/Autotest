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
        u"""PC—输入新密码界面，只输入确认密码"""
        logger.info("点击修改密码")
        fgt_psd = Common.get_element_by_class_name_and_text(self, "a", "", "忘记密码")
        Common.touch_by_element(self, fgt_psd)

        logger.info("查看是否进入修改密码界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.checkUpdatePwdcodeBtn))

        logger.info("输入手机号获取验证码")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入手机号", Content.register_count)
        Common.touch_by_id(self, ID.getUpdatePwdCodeBtn)
        ident_code = Common.get_identifying_code(self, Content.register_count)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入验证码", ident_code)
        Common.touch_by_id(self, ID.checkUpdatePwdcodeBtn)

        logger.info("查看是否进入新密码界面")
        text_list = Common.get_text_by_class_name(self, ClassName.label, "label")
        self.assertTrue(Common.check_text_in_list(self, text_list, "新密码"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "确认密码"))

        logger.info("只输入新密码，点击确定")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "确认密码", Content.login_password)
        Common.touch_by_id(self, ID.updatePasswordBtn)

        logger.info("查看是否有错误提示")
        err_tip = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, err_tip, "密码不能为空"))

