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
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.del_sechdule_by_name(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""在日程界面点击您的位置后的服务，可以返回服务界面"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "服务")
        Common.wait(self, 2)

        logger.info("点击任务")
        Common.touch_text_by_class_name(self, ClassName.center, "日程")

        logger.info("判断是否进入日程界面")
        text = Common.get_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "span")[0]
        self.assertEqual(text, "日程")

        logger.info("点击‘您的’后面的‘服务’，可以返回服务界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "服务", "a")

        logger.info("判断是否返回服务界面")
        item_list = Common.get_text_by_class_name(self, ClassName.ivu_menu_item_active_selected, "li")
        res = Common.check_text_in_list(self, item_list, "服务")
        self.assertTrue(res)


 
    
