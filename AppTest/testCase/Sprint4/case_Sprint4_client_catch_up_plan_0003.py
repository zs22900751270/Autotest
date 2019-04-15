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
        u"""首页下方推荐APP显示"""
        logger.info("输入账号密码进行登录")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("查看下方是否有推荐APP")
        self.assertTrue(Common.check_if_class_name_exist(self, ClassName.wrap, "div"))



    
