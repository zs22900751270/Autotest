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
        u"""新发送消息通知、系统消息、系统公告"""
        logger.info("登录client端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击进入系统消息界面")
        res_ele = Common.get_result_by_class_name_blank(self, "div", ClassName.user_info)
        Common.touch_tag_name_by_element(self, res_ele, "img", 2)

        logger.info("判断是否进入消息界面")
        text_list = Common.get_text_by_class_name(self, ClassName.user_menu, "div")
        res1 = Common.check_text_in_list(self, text_list, "通知")
        res2 = Common.check_text_in_list(self, text_list, "系统消息")
        res3 = Common.check_text_in_list(self, text_list, "系统公告")
        if res1 and res2 and res3:
            self.assertTrue(True)
        else:
            self.assertTrue(False)



    
