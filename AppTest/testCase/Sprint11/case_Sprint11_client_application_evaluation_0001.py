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
        u"""PC端-游客模式应用评论验证"""
        logger.info("不登录，点击应用市场")
        app_name = Common.get_frist_app_name(self)
        Common.touch_by_id(self, ID.toMarket)

        logger.info("点击进入应用详情")
        tab_hit = Common.get_result_by_class_name_blank(self, "ul", ClassName.tab_tit)
        Common.touch_tag_name_by_element(self, tab_hit, "li", 2)
        Common.open_app_detail_by_by_name(self, app_name)
        tab_title = Common.get_result_by_class_name_blank(self, "div", ClassName.tab_title)
        Common.touch_tag_name_by_element(self, tab_title, "span", 3)

        logger.info("查看是否出现应用评论输入框")
        textarea = Common.get_elements_by_placeholder_and_class_name(self, ClassName.ivu_input, "请填写应用评论")
        self.assertEqual(len(textarea), 0)



