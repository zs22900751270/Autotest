#!/usr/bin/env python
# _*_coding:utf-8_*_

from AppTest.Common import *
long_theme_name = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
theme_name = "theme_add_01"


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
        u"""主题分类选择"""
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
        sel_ele = Common.get_class_name_elements_by_element_blank(self, ul_ele, "li", ClassName.ivu_select_item)
        Common.touch_text_by_elements(self, sel_ele, "政府/事业单位")
        Common.wait(self, 3)

        logger.info("点击保存")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("点击分类")
        industry = Common.get_results_by_class_name(self, ClassName.ivu_select_placeholder)[0]
        Common.touch_by_element(self, industry)
        ul_ele1 = Common.get_results_by_class_name_blank(self, "ul", ClassName.ivu_select_dropdown_list)[0]
        sel_ele1 = Common.get_class_name_elements_by_element_blank(self, ul_ele1, "li", ClassName.ivu_select_item)
        Common.touch_text_by_elements(self, sel_ele1, "政府/事业单位")

        logger.info("判断是否搜索成功")
        text_list = Common.get_text_by_class_name(self, ClassName.ivu_table_cell, "div")
        logger.info(text_list)
        result = Common.check_text_in_list(self, text_list, theme_name)
        self.assertTrue(result)



    
