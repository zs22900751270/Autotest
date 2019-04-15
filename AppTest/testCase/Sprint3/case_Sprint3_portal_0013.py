#!/usr/bin/env python
# _*_coding:utf-8_*_


from AppTest.Common import *
theme_name = "zhangsen"


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.case_name = os.path.basename(__file__)
        browse = BrowserEngine(self)
        self.web_driver = browse.open_browser(self, url=WebControlServer.web_url)

    @classmethod
    def tearDown(self):
        logger.info("清除所创建的字典")
        Common.report_screen_shot(self, self.case_name)
        Common.connect_sql(self, "delete from dict_theme where name='%s'" % theme_name, "scap")
        Common.quit(self)

    def test_step(self):
        u"""数据标准字典可以正常添加字段"""
        logger.info("web端登录")
        Common.login_web_portal(self, Content.register_count, Content.login_password)

        logger.info("判断是否登陆成功")
        get_login_result = Common.check_if_class_name_exist(self, ClassName.ivu_icon_log_out, "i")
        self.assertTrue(get_login_result)

        logger.info("点击大数据管理,创建标准字典")
        Common.touch_text_by_class_name(self, ClassName.ivu_menu_item, "大数据管理", "li")

        logger.info("进入数据字典主题界面")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "标准数据字典管理", "span")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "数据字典主题", "span")

        logger.info("点击添加主题")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加主题", "button")

        logger.info("输入主题名称和分类, 点击保存")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入主题名称", theme_name)
        result = Common.get_results_by_class_name_blank(self, "span", ClassName.ivu_select_placeholder)
        Common.touch_by_element(self, result[-1])
        chioce_list = Common.get_results_by_class_name_blank(self, "ul", ClassName.ivu_select_dropdown_list)[-1]
        type_list = Common.get_class_name_elements_by_element_blank(self, chioce_list, "li", ClassName.ivu_select_item)
        Common.touch_by_element(self, type_list[0])
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        logger.info("点击标准数据字典")
        Common.touch_text_by_class_name(self, ClassName.layout_text, "标准数据字典")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_primary, "添加字典", "button")

        logger.info("输入标准字典所需参数")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_placeholder, "请选择")
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, theme_name)
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入库名称", "database_name")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入表名称", "table_name")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入字段名称", "str_name")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input, "请输入字段描述", "str_dis_name")
        select = Common.get_results_by_class_name_blank(self, "span", ClassName.ivu_select_placeholder)[-1]
        Common.touch_by_element(self, select)
        Common.touch_text_by_class_name(self, ClassName.ivu_select_item, "text")
        Common.send_text_by_class_name_and_palceholder(self, ClassName.ivu_input_number_input, "请输入字段长度", "50")
        Common.touch_text_by_class_name(self, ClassName.ivu_radio_wrapper_group_item, "是", "label")
        Common.touch_text_by_class_name(self, ClassName.ivu_btn_large, "确定", "button")

        result = Common.get_text_by_class_name(self, ClassName.ivu_form_item_error_tip, "div")
        self.assertTrue("请输入字段含义" in result)



     
