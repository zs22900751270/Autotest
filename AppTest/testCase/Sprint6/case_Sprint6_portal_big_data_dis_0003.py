#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


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
        u"""导航栏点击服务"""
        logger.info("打开App")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        Common.wait(self, 2)

        logger.info("点击大数据展示")
        if Common.get_display_status_by_text(self, "图表设计"):
            Common.touch_text_by_class_name(self, ClassName.layout_text, "大数据展示")
            Common.wait(self, 2)

        logger.info("点击图标设计")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "图表设计")
        Common.wait(self, 2)

        logger.info("点击添加资源框")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加资源框", "button")
        resource = Common.get_results_by_class_name_blank(self, "div", ClassName.vue_grid_item_resizable)

        logger.info("判断是否添加成功")
        self.assertEqual(len(resource), 1)

        logger.info("点击删除按钮")
        Common.move_mouse_on(self, resource[0])
        del_btn = Common.get_results_by_class_name_blank(self, "div", ClassName.btn_span)[0]
        Common.move_mouse_on(self, del_btn)
        Common.touch_by_element(self, del_btn)

        logger.info("判断是否删除成功")
        resource1 = Common.get_results_by_class_name_blank(self, "div", ClassName.vue_grid_item_resizable)
        logger.info(len(resource1))
        self.assertEqual(len(resource1), 0)



    
