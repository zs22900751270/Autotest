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
        Common.quit(self)

    def test_step(self):
        u"""我的资料界面修改密码"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("进入我的界面")
        me_ele = Common.get_result_by_class_name(self, ClassName.avator)
        Common.touch_by_element(self, me_ele)
        id_result = Common.get_result_by_id(self, ID.panelMenu)
        Common.touch_tag_name_by_element(self, id_result, "li", 4)

        logger.info("进入修改账号密码界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "修改账号密码", "li")

        logger.info("输入验证码，点击下一步")
        Common.touch_by_id(self, ID.getCodeFormCodeBtn)
        identify_code = Common.get_identifying_code(self, Content.register_count)
        res_1 = Common.get_result_by_class_name_blank(self, "div", ClassName.checkCodeInp_toleft_ivu_input_wrapper_type)
        input_ele = Common.get_tag_name_by_element(self, res_1, "input")
        Common.send_text_by_element(self, input_ele, identify_code)
        Common.touch_by_id(self, ID.codeFormNextBtn)

        logger.info("查看是否进入输入密码界面")
        tit_text = Common.get_text_by_class_name(self, ClassName.title, "div")
        self.assertTrue(Common.check_text_in_list(self, tit_text, "修改账号密码"))

        logger.info("只输入新密码，不输入确认密码")
        input_list = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)
        Common.send_text_by_element(self, input_list[0], Content.login_password)
        Common.send_text_by_element(self, input_list[1], Content.login_password)

        logger.info("查看是否有错误提示")
        Common.touch_by_id(self, ID.pwdFormOkBtn)

        logger.info("查看是否修改成功")
        tip_list = Common.get_text_by_class_name(self, ClassName.tit)
        self.assertTrue(Common.check_text_in_list(self, tip_list, "密码修改成功"))

