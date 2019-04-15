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
        u"""web页面输入正常手机号和密码"""
        logger.info("登录客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("判断是否登录成功")
        self.assertTrue(Common.check_if_class_name_exist(self, ClassName.user_info))



     
