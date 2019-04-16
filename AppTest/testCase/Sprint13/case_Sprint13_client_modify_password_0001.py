#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        # Common.quit(self)

    def test_step(self):
        u"""PC—修改手机号界面输入已过期的验证码"""
        logger.info("登录后端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("进入修改密码界面")
        me_ele = Common.get_result_by_class_name(self, ClassName.avator)
        Common.touch_by_element(self, me_ele)
        id_result = Common.get_result_by_id(self, ID.panelMenu)
        Common.touch_tag_name_by_element(self, id_result, "li", 4)
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "修改账号密码", "li")

        logger.info("查看是否进入修改密码界面")
        text_1 = Common.get_text_by_class_name(self, ClassName.title, "div")
        self.assertTrue(Common.check_text_in_list(self, text_1, "修改账号密码"))

        logger.info("点击获取验证码")
        Common.touch_by_id(self, ID.getCodeFormCodeBtn)

        logger.info("后台获取验证码并输入")
        ident_code = Common.get_identifying_code(self, Content.register_count)
        input_ele = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)
        Common.send_text_by_element(self, input_ele[0], ident_code)
        Common.touch_by_id(self, ID.codeFormNextBtn)

        logger.info("查看是否进入修改密码界面")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_label, "label")
        self.assertTrue(Common.check_text_in_list(self, text_list, "新密码"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "确认新密码"))

        logger.info("点击纯数字新密码，查看是否会有报错提示")
        input_ele = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)
        Common.send_text_by_element(self, input_ele[0], "1111111")
        Common.touch_by_id(self, ID.pwdFormOkBtn)
        err_tip = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, err_tip, "密码只包括6-32位的字符和数字"))

        logger.info("点击纯英文新密码，查看是否会有报错提示")
        input_ele = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)
        Common.send_text_by_element(self, input_ele[0], "aaaaaa")
        Common.touch_by_id(self, ID.pwdFormOkBtn)
        err_tip = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, err_tip, "密码只包括6-32位的字符和数字"))
