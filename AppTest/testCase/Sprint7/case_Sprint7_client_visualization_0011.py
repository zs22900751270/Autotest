#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
title = "new_fl"


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
        Common.del_report_template_by_user(self, Content.register_count)
        Common.quit(self)

    def test_step(self):
        u"""导航栏点击服务"""
        logger.info("打开客户端")
        Common.login_web_client(self, Content.register_count, Content.login_password)

        logger.info("点击服务")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "服务")
        Common.wait(self, 2)

        logger.info("点击数据可视化")
        Common.touch_text_by_class_name(self, ClassName.center, "数据可视化")
        Common.wait(self, 2)

        logger.info("判断是否进入数据可视化界面")
        result = Common.check_if_class_name_exist(self, ClassName.no_html_text, "div")
        self.assertTrue(result)

        logger.info("点击添加模板")
        tr = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_tabs_tab)
        Common.touch_by_element(self, tr[0])
        item_results = Common.get_results_by_class_name_blank(self, "div", ClassName.tpl_item)
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_tooltip_rel, "div")
        settings_item = Common.get_results_by_class_name_blank(self, "i", ClassName.fa_plus_circle)

        for i in range(len(item_results)):
            Common.move_mouse_on(self, item_results[i])
            Common.touch_by_element(self, settings_item[i])

        logger.info("判断是否添加成功")
        tr = Common.get_results_by_class_name_blank(self, "div", ClassName.ivu_tabs_tab)
        Common.touch_by_element(self, tr[0])
        item_result1 = Common.get_text_by_class_name(self, ClassName.ivu_tooltip_rel, "div")
        new = list(filter(None, item_result1))
        self.assertEqual(text_list, new)


 

