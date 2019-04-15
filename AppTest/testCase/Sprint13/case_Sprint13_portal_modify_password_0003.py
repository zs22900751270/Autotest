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
        u"""PC-修改密码界面获取验证码按钮可点"""
        logger.info("登录后端")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击修改密码")
        per_info = Common.get_result_by_class_name_blank(self, "div", ClassName.set_personal_info)
        Common.touch_tag_name_by_element(self, per_info, "a", 1)

        logger.info("查看是否进入修改密码界面")
        text_1 = Common.get_text_by_class_name(self, ClassName.title, "h3")
        self.assertTrue(Common.check_text_in_list(self, text_1, "修改账号密码"))

        logger.info("点击获取验证码")
        Common.touch_by_id(self, ID.getCodeFormCodeBtn)
        ident_code = Common.get_identifying_code(self, Content.register_count)
        self.assertIsNotNone(ident_code)

