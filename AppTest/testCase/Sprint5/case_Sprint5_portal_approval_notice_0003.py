#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
classification = "new_sen"
classification_long = "sprint_notice_5_1ssssss"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        Common.report_screen_shot(self, self.case_name)
        logger.info("收尾工作")
        Common.quit(self)

    def test_step(self):
        u"""通知管理页面点击所有分类下方显示所有分类"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击运维管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "运维管理")
        Common.wait(self, 2)

        logger.info("判断是否存在分类")
        left_ele = Common.get_result_by_class_name_blank(self, "div", ClassName.left)
        list_left = Common.get_class_name_elements_by_element_blank(self, left_ele, "li", ClassName.ivu_menu_item)
        logger.info(Common.get_text_by_elements(self, list_left))
        self.assertIsNotNone(list_left)



    
