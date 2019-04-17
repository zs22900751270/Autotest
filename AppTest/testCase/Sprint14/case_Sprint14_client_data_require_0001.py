#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.filterwarnings("ignore")
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControl.web_url)

    @classmethod
    def tearDown(self):
        logger.info("收尾工作")
        Common.report_screen_shot(self, self.case_name)
        Common.quit(self)

    def test_step(self):
        u"""Client端-数据需求展示"""
        logger.info("不登录进入数据开放界面")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "数据开放", "li")

        logger.info("查看是否可以进入数据开放界面")
        text_list = Common.get_text_by_class_name(self, ClassName.title, "span")
        self.assertTrue(Common.check_text_in_list(self, text_list, "数据总览："))

        logger.info("点击数据需求的“更多”")
        more_ele = Common.get_results_by_class_name(self, ClassName.more)
        Common.touch_by_element(self, more_ele[2])

        logger.info("点击发布需求，跳转至登录界面")
        Common.touch_text_by_class_name(self, ClassName.blue_btn_opertion_ivu_btn, "发布需求", "button")

        logger.info("查看是否成功跳转至登录界面")
        self.assertTrue(Common.check_if_id_exist(self, ID.handleSubmitBtn))




