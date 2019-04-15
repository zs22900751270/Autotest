#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""平台统计页面左侧导航栏显示正确"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理,点击数据集管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "运维管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "平台统计", "span", 1)
        Common.touch_text_by_class_name(self, ClassName.layout_text, "平台统计", "span", 2)

        text = Common.get_text_by_class_name(self, ClassName.menu_title, "div")
        self.assertTrue("平台统计" in text)



    
