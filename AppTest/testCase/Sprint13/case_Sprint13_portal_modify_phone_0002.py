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
        u"""PC-修改界面存在新手机号输入框，验证码输入框与验证码按钮"""
        logger.info("登录后端")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击修改密码")
        per_info = Common.get_result_by_class_name_blank(self, "div", ClassName.set_personal_info)
        Common.touch_tag_name_by_element(self, per_info, "a", 2)

        logger.info("查看是否进入修改密码界面")
        text_1 = Common.get_text_by_class_name(self, ClassName.title, "h3")
        self.assertTrue(Common.check_text_in_list(self, text_1, "修改验证手机号"))

        logger.info("点击替换")
        Common.touch_text_by_class_name(self, ClassName.toright, "替换", "div")

        logger.info("查看元素是否存在")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_label, "label")
        self.assertTrue(Common.check_text_in_list(self, text_list, "新手机号码"))
        self.assertTrue(Common.check_text_in_list(self, text_list, "手机验证码"))
        self.assertTrue(Common.check_if_id_exist(self, ID.getPhoneFormCodeBtn))
        self.assertTrue(Common.check_if_id_exist(self, ID.changePhoneBtn))



