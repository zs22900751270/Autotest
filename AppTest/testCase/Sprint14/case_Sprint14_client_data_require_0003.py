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
        u"""Client端-需求详情页面"""
        logger.info("不登录进入数据开放界面")
        Common.login_web_client(self, Content.register_count, Content.login_password)
        Common.touch_by_id(self, ID.dataOpen)

        logger.info("点击发布需求的“更多”")
        more_list = Common.get_results_by_class_name(self, ClassName.more)
        Common.touch_by_element(self, more_list[2])

        logger.info("点击发布需求")
        Common.touch_text_by_class_name(self, ClassName.blue_btn_opertion_ivu_btn, "发布需求", "button")


