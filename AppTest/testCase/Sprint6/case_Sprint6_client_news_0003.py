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
        u"""界面右上角未读消息"""
        logger.info("登录client端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入系统消息界面")
        res_ele = Common.get_result_by_class_name_blank(self, "div", ClassName.user_info)
        Common.touch_tag_name_by_element(self, res_ele, "img", 2)

        logger.info("判断是否进入消息界面")
        text_list = Common.get_text_by_class_name(self, ClassName.num)
        num1 = int(text_list[-1])
        num2 = int(text_list[-2])
        num3 = int(text_list[-3])
        num4 = int(text_list[-4])
        self.assertEqual(num1+num2+num3, num4)



    
