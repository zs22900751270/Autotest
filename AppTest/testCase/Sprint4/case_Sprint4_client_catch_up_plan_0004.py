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
        u"""应用合集中精选热门推荐显示正确"""
        logger.info("输入账号密码进行登录")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击应用集合界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "应用市场")
        Common.touch_text_by_class_name(self, ClassName.more, "更多>>", "a")

        logger.info("检测是否进入热门界面")
        self.assertTrue(Common.check_if_class_name_exist(self, ClassName.app_more_list), "div")



