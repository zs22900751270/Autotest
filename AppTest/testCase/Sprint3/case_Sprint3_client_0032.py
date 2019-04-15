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
        u"""web默认不勾选用户协议"""
        logger.info("点击注册")
        Common.touch_text_by_class_name(self, ClassName.ivu_col_offset_19, "注册账号", "div")
        logger.info("判断是否默认不勾选用户协议")
        user_procotol = Common.get_result_by_class_name_blank(self, "input", ClassName.ivu_checkbox_input)
        element_result = user_procotol.get_attribute("class")
        final_result = False
        if "checked" not in element_result:
            final_result = True
        self.assertTrue(final_result)



     
