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
        logger.info("收尾工作")
        Common.quit(self)

    def test_step(self):
        u"""在新建任务界面，点击你的位置后的服务和任务"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_by_id(self, ID.toService)

        logger.info("点击任务")
        Common.touch_by_id(self, ID.taskBtn)

        logger.info("判断是否进入任务界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.createTask))

        logger.info("在新建任务界面，点击‘任务’，可以返回任务界面")
        Common.touch_by_id(self, ID.createTask)
        Common.touch_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "任务", "a")

        logger.info("判断是否可以返回任务界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.createTask))

        logger.info("在新建任务界面，点击‘任务’，可以返回任务界面")
        Common.touch_by_id(self, ID.createTask)
        Common.touch_text_by_class_name(self, ClassName.ivu_breadcrumb_item_link, "服务", "a")

        logger.info("判断是否可以返回任务界面")
        text_con = Common.get_result_by_id(self, ID.toService)
        self.assertEqual("服务", Common.get_text_by_element(self, text_con))


 
    
