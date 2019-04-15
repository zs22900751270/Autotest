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
        u"""PC—忘记密码输入相同的纯数字或者纯字母新密码与确认密码"""
        logger.info("登录后端")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击修改密码")
        per_info = Common.get_result_by_class_name_blank(self, "div", ClassName.set_personal_info)
        Common.touch_tag_name_by_element(self, per_info, "a", 1)

        logger.info("查看是否进入修改密码界面")
        text_1 = Common.get_text_by_class_name(self, ClassName.title, "h3")
        self.assertTrue(Common.check_text_in_list(self, text_1, "修改账号密码"))

        logger.info("等待5分钟之后输入验证码")
        Common.touch_by_id(self, ID.getCodeFormCodeBtn)
        input_ele = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)
        ident_code = Common.get_identifying_code(self, Content.register_count)
        Common.send_text_by_element(self, input_ele[0], ident_code)
        Common.touch_by_id(self, ID.codeFormNextBtn)

        logger.info("查看是否进入新密码界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_label, "label")
        self.assertTrue(Common.check_text_in_list(self, text_list, "新密码"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "确认新密码"))

        logger.info("输入纯数字密码,点击确定")
        psd_ele = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)
        Common.send_text_by_element(self, psd_ele[0], "1111111")
        Common.send_text_by_element(self, psd_ele[1], "1111111")
        Common.touch_by_id(self, ID.pwdFormOkBtn)

        logger.info("查看是否有错误提示")
        err_tip = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(Common.check_text_in_list(self, err_tip, "密码只包括6-32位的字符和数字"))

        logger.info("输入纯数字密码,点击确定")
        psd_ele = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)
        Common.send_text_by_element(self, psd_ele[0], "aaaaaa")
        Common.send_text_by_element(self, psd_ele[1], "aaaaaa")
        Common.touch_by_id(self, ID.pwdFormOkBtn)

        logger.info("查看是否有错误提示")
        err_tip = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip)
        self.assertTrue(Common.check_text_in_list(self, err_tip, "密码只包括6-32位的字符和数字"))

