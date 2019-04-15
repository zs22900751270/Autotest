#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
theme_name = "theme_add_01"
theme_name_new = "theme_add_new"


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
        Common.connect_sql(self, "DELETE FROM dict_theme WHERE NAME='%s'" % theme_name, "scap")
        Common.quit(self)

    def test_step(self):
        u"""删除审批流程"""
        logger.info("输入账号密码进行登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("点击大数据管理")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理")
        Common.wait(self, 2)

        logger.info("点击标准数据字典管理")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "标准数据字典管理")
        Common.wait(self, 2)

        logger.info("点击数据字典主题")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据字典主题")
        Common.wait(self, 2)

        logger.info("点击添加主题，只输入一项，不能成功创建")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加主题", "button")

        logger.info("输入主题名称")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入主题名称", theme_name)

        logger.info("选择行业分类")
        industry = Common.get_results_by_class_name(self, ClassName.ivu_select_placeholder)[1]
        Common.touch_by_element(self, industry)
        ul_ele = Common.get_results_by_class_name_blank(self, "ul", ClassName.ivu_select_dropdown_list)[-1]
        sel_ele = Common.get_class_name_elements_by_element_blank(self, ul_ele, "li", ClassName.ivu_select_item)[0]
        Common.touch_by_element(self, sel_ele)
        Common.wait(self, 3)

        logger.info("点击保存")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("搜索主题名称")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "主题名称", theme_name)
        search_button = Common.get_results_by_class_name_blank(self, "i", ClassName.search_icon)[0]
        Common.touch_by_element(self, search_button)
        Common.wait(self, 2)

        logger.info("删除所创建数据")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_error_small, "删除", "button")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("判断是否删除成功")
        Common.wait(self, 3)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "主题名称", theme_name)
        search_button = Common.get_results_by_class_name_blank(self, "i", ClassName.search_icon)[0]
        Common.touch_by_element(self, search_button)
        search_result1 = Common.get_results_by_class_name(self, ClassName.ivu_table_row)
        self.assertTrue(len(search_result1) == 0)



    
