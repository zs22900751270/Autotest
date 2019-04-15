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
        u"""输入已使用的的手机号"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("进入我的界面")
        me_ele = Common.get_result_by_class_name(self, ClassName.avator)
        Common.touch_by_element(self, me_ele)
        id_result = Common.get_result_by_id(self, ID.panelMenu)
        Common.touch_tag_name_by_element(self, id_result, "li", 4)

        logger.info("进入修改手机号界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "修改验证手机号", "li")

        logger.info("检测是否进入修改手机号界面")
        tit_text = Common.get_text_by_class_name(self, ClassName.title)
        self.assertTrue(Common.check_text_in_list(self, tit_text, "修改验证手机号"))

        logger.info("点击替换，输入错误的手机号")
        Common.touch_text_by_class_name(self, ClassName.toright, "替换")
        input_list = Common.get_results_by_class_name_blank(self, "input", ClassName.ivu_input)
        Common.send_text_by_element(self, input_list[-2], Content.register_count)

        logger.info("查看是否提示手机号输入错误")
        Common.touch_by_id(self, ID.getPhoneFormCodeBtn)
        err_list = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue(Common.check_text_in_list(self, err_list, "用户已存在"))


