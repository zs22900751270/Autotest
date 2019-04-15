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
        u"""进入应用后观察应用信息"""
        logger.info("输入账号密码进行登录")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击应用集合界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "应用市场")

        logger.info("进入应用详情界面")
        app_icon = Common.get_result_by_class_name_blank(self, "img", ClassName.app_icon)
        Common.touch_by_element(self, app_icon)

        logger.info("判断是否进入应用详情界面")
        res = Common.get_text_by_class_name(self, ClassName.active_tit, "span")
        self.assertTrue("应用详情" in res)

